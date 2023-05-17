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

## _So why this tool?_
It's well known that most of the time, the hidden gem aka Blind SQLi vulnerability found inside sitemap page. You just need to find the correct parameter and the magic would happen. You can use this tool in conjunction with other to scan valid sitemap urls and get a head start in bug bounty game.

By leveraging this tool, you can efficiently explore sitemaps and increase your chances of uncovering critical vulnerabilities. It would a valuable addition to your bug hunting toolkit, empowering you to find those elusive Blind SQLi vulnerabilities that may have gone unnoticed. Don't miss out on this opportunity to level up your bug bounty skills!

**Bonus:** It's mostly the offset guy 😎