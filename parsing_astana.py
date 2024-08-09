# import requests

# url = "https://www.weather-forecast.com/locations/Astana/forecasts/latest"

# response = requests.get(url)
# html = response.text

# with open('weather.html', "w", encoding="utf-8") as file:
#     file.write(html)

html = """class="b-metar-table__weather-station-name"><a href="/weather-stations/Astana">Astana/Akmola Астана</a></strong> </div><div class="b-metar-table__weather-station-detail"><span class="dist">11</span> <span class="dist">km</span> <span class="dist">SW</span></div><div class="b-metar-table__weather-station-elevation"><span><span class="dist">239</span><span class="dist">m</span> alt.</span></div><div class="dist">3 hours ago</div></td><td class="b-metar-table__temperature"><div class="b-metar-table__temperature-value temp-color3"><span class="dist">28.1</span>&deg;&thinsp;<span class="dist">C</span></div></td><td """

lines_span = html.split('<span class="dist">')

print("Astana")
num_line = lines_span[1].split("</span>")[0]
m_line = lines_span[2].split("</span>")[0]
SW_line = lines_span[3].split("</span>")[0]
num2_line = lines_span[4].split("</span>")[0]
m2_line = lines_span[5].split("</span>")[0]
temperatur_line = lines_span[6].split("</span>")[0]
C_line = lines_span[7].split("</span>")[0]

print(num_line, m_line, SW_line)
print(num2_line, m2_line)
print(temperatur_line, C_line)

print(lines_span)