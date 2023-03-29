---
layout: post
title: how to run this repo locally
category: technical
---

geek understands the meaning of doing geek stuff

```sh
# Development
# http://localhost:4000
bundle install
bundle exec jekyll serve

# other
bundle exec jekyll serve --config _config_dev.yml
bundle exec jekyll build
bundle exec jekyll build --config _config_dev.yml
```

```sh
git clone git@github.com:igorlima/unapologetic-thoughts.git
```

```sh
# Ruby Docker
# https://hub.docker.com/_/ruby/tags
sudo docker run \
  -it -p 8080:8080 \
  --name my-ruby \
  --mount src=`pwd`,target=/home/local,type=bind \
  --workdir /home/local \
  --rm ruby:alpine3.17 sh
```

----

Jekyll on macOS [^1] - how to install

```sh
# install chruby and the latest Ruby with ruby-installPermalink
brew install chruby ruby-install xz
ruby-install ruby 3.1.3
```

```sh
# configure the shell to automatically use chruby
echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
echo "chruby ruby-3.1.3" >> ~/.zshrc # run 'chruby' to see actual version

# manually configure the shell to use chruby
source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh
source $(brew --prefix)/opt/chruby/share/chruby/auto.sh
chruby ruby-3.1.3
```

```sh
ruby -v
gem install jekyll

gem install no-style-please
```

----

---
{: data-content="footnotes"}

[^1]: [Jekyll on macOS](https://jekyllrb.com/docs/installation/macos/)
