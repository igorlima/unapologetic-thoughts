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

Jekyll on Linux [^2] - how to install

```sh
# install gpg keys
gpg --keyserver keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
# install rvm (development version)
\curl -sSL https://get.rvm.io | bash
# install ruby
rvm list known
# rvm install "ruby-3.1.3"
```

```
# manually configure the shell to use rvm
source /home/opc/.rvm/scripts/rvm
# rvm use "ruby-3.1.3"
```

----

---
{: data-content="footnotes"}

[^1]: [Jekyll on macOS](https://jekyllrb.com/docs/installation/macos/)
[^2]: [Installing RVM](https://rvm.io/rvm/install)
