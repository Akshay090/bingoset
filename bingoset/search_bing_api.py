from requests import exceptions
import requests
from PIL import Image
import os
from pathlib import Path
import os
from urllib.parse import urlparse


from bingoset.utilities.checks import check_config

# MAX_RESULTS = 250
# GROUP_SIZE = 50


def get_images_bing(search_term, MAX_RESULTS, GROUP_SIZE):
    API_KEY = check_config()

    URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

    EXCEPTIONS = {
        IOError,
        FileNotFoundError,
        exceptions.RequestException,
        exceptions.HTTPError,
        exceptions.ConnectionError,
        exceptions.Timeout,
    }

    headers = {"Ocp-Apim-Subscription-Key": API_KEY}
    params = {"q": search_term, "offset": 0, "count": GROUP_SIZE}

    # make the search
    print("[INFO] searching Bing API for '{}'".format(search_term))
    search = requests.get(URL, headers=headers, params=params)
    search.raise_for_status()

    results = search.json()
    estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
    print("[INFO] {} total results for '{}'".format(estNumResults, search_term))

    # initialize the total number of images downloaded thus far
    total = 0

    # loop over the estimated number of results in `GROUP_SIZE` groups
    for offset in range(0, estNumResults, GROUP_SIZE):
        # update the search parameters using the current offset, then
        # make the request to fetch the results
        print(
            "[INFO] making request for group {}-{} of {}...".format(
                offset, offset + GROUP_SIZE, estNumResults
            )
        )
        params["offset"] = offset
        search = requests.get(URL, headers=headers, params=params)
        search.raise_for_status()
        results = search.json()
        print(
            "[INFO] saving images for group {}-{} of {}...".format(
                offset, offset + GROUP_SIZE, estNumResults
            )
        )

        # loop over the results
        for v in results["value"]:
            # try to download the image
            try:
                # make a request to download the image
                print("[INFO] fetching: {}".format(v["contentUrl"]))
                r = requests.get(v["contentUrl"], timeout=30)

                # build the path to the output image
                # ext = v["contentUrl"][v["contentUrl"].rfind(".") :]
                url_path = urlparse(v["contentUrl"]).path
                ext = os.path.splitext(url_path)[1]

                dataset_path = Path.cwd() / "dataset" / search_term
                path_out_img = dataset_path / f"{str(total).zfill(8)}{ext}"
                dataset_path.mkdir(parents=True, exist_ok=True)

                # write the image to disk
                f = open(path_out_img, "wb")
                f.write(r.content)
                f.close()

            # catch any errors that would not unable us to download the
            # image
            except Exception as e:
                # check to see if our exception is in our list of
                # exceptions to check for
                print(e)
                if type(e) in EXCEPTIONS:
                    print("[INFO] skipping: {}".format(v["contentUrl"]))
                    continue

            try:
                im = Image.open(path_out_img)
            except IOError:
                # filename not an image file, so it should be ignored
                print("[INFO] deleting: {}".format(path_out_img))
                os.remove(path_out_img)
                continue

            # update the counter
            total += 1


