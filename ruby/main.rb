require 'net/http'
require 'json'
require 'cgi'

def delimiter(number)
  number.reverse.scan(/.{1,3}/).join(',').reverse
end

while (true) do
  uri = URI('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

  response = Net::HTTP.get(uri)
  response_json = JSON.parse(response, symbolize_names: true)

  puts "Porcentagem geral: #{response_json[:pst]}%"
  puts "#{'Nome'.ljust(20)} | #{'Votos'.ljust(16)} | Porcentagem"
  response_json[:cand].each do |candidate|
    name = CGI.unescapeHTML(candidate[:nm])
    puts "#{name.ljust(20)} | #{delimiter(candidate[:vap]).ljust(16)} | #{candidate[:pvap]}%"
  end
  sleep 10
  puts "*" * 60
end

