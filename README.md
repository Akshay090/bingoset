<h4 align="center">
    <a href="https://github.com/Akshay090/bingoset">
        <img src="https://raw.githubusercontent.com/Akshay090/bingoset/master/.github/bingoset-banner.png" alt="bingoset" />
    </a>
    <br>
    <br>
     CLI Toolkit to quickly create image dataset using Bing Image Search API

![PyPI - License](https://img.shields.io/pypi/l/bingoset?style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bingoset)
![Twitter Follow](https://img.shields.io/twitter/follow/aks2899?style=social) 

</h4>

# Welcome to BingoSet 


## Install

```sh
pip3 install bingoset
```
## Set-up

Get your Bingo Image Search API key and execute below command

```sh
bingoset set-api-key YOUR_BING_API_KEY_HERE
```

## Usage 

```sh
bingoset q pikachu
```
This will download 250 (default) images of pikachu into a directory called dataset (default)

## Additional Config

```sh
bingoset set-max-results 100
```
Change the number of images you want to download, eg : 100

```sh
bingoset set-group-size 20
```
Change the group size of images you want to download, eg : 100
