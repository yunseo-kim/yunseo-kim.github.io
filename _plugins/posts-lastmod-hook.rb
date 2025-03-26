#!/usr/bin/env ruby
#
# Check for changed posts
 
require 'date'

Jekyll::Hooks.register :posts, :post_init do |post|

  commit_num = `git rev-list --count HEAD "#{ post.path }"`

  if commit_num.to_i > 1
    lastmod_date = `git log -1 --pretty="%ad" --date=iso "#{ post.path }"`
    holocene_lastmod_date = lastmod_date.sub(/(\d{4})/) do |year|
      (year.to_i + 10000).to_s
    end
    post.data['last_modified_at'] = holocene_lastmod_date
  end

end
