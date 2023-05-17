# SitemapUp (sup)
A simple and fast tool to check the validity of sitemap within a website/url.

## Installing

### Clone repo:
```sh
gh repo clone hamza-avvan/sup
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

Or use this command:
```sh
python3 -m pip install termcolor 
```

## Usage
```sh
python3 sup.py filetoscan.txt [-o outfile.txt]
```

![SUP in action](https://github.com/hamza-avvan/sup/blob/main/images/ss1.jpeg?raw=true)

A sample usage of **sup**:
```sh
gau example.com > urls.txt; cat urls.txt | grep -i sitemap > sitemapurls.txt | sort sitemapurls.txt | uniq > sitemapurls.txt
python3 sup.py sitemapurls.txt
```