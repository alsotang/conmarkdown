# coding=utf-8
def parse_html_block(html_data)
  #html_data.gsub!(/(?:<(.*?)(\s+.*?>|>)(.*?)<\/\1>)|(?:<(.*?)\s+(\/>))/m) do 
  html_data.gsub!(/(?:<(.*?)\s+(\/>))|(?:<(.*?)(\s+.*?>|>)(.*?)<\/\1>)/m) do 

    tag, attrs, content = $1, $2, ($3 or '')
    case tag
    when 'p', 'ol'
      content += "\n"
    when 'li'
      content = '* ' + content
    when 'code'
      content = '`' + content + '`'
    when 'a'
      href = ''
      title = ''
      attrs.scan(/\s+(.*?)=(".*")/) do 
        case $1
        when 'href'
          href = $2.gsub('"', '')
        when 'title'
          title = $2
        end
      end
      content = '[' + content + '](' + a = [href, title].join(' ') + ')'
    end
    puts tag, attrs, content
    gets
    content = parse_html_block(content)
  end
  return html_data

end


filename = 'test'
html_data = open(filename + '.html') do |f|
              f.read
            end 
html_data.gsub!(/^\s*/, '') #消除行首的indent


#html_data = parse_html_block(html_data) 

open(filename + '_converted.md', 'w') do |wf|
  wf.print html_data
end


