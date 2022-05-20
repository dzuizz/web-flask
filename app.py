from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# ABCDEFGHIJKLMNOPQRSTUVWXYZ

contests = {
	'AMC': 'Australian Mathematics Olympiad',
	'AMO': 'American Mathematics Olympiad',
	'BEBRAS': 'International Challenge on Informatics and Computational Thinking',
	'DOKA': 'Depth Of Knowledge Assesment',
	'DrCT': 'Doctor Of Computational Thinking',
	'DrCT Global Finals': 'Doctor Of Computational Thinking',
	'ICAS Science': 'A Science Contest',
	'IJMO': 'International Junior Mathematical Olympiad',
	'iOS App Development with Swift Essential': 'InfoTech',
	'Kumon ASHR English': 'Advanced Student Honour Roll',
	'Kumon ASHR Mathematics': 'Advanced Student Honour Roll',
	'NMOS by NUS High School': 'National Mathematical Olympiad of Singapore',
	'RIPMWC by Raffles Institution': 'Raffles Institution Primary Mathematics World Contest',
	'SASMO': 'Singapore and Asian Schools Mathematical Olympiad',
	'SEF': 'Scholastic Environmental Fund - theme: "Youth Taking Action to Prevent Negative Impact on Non-Human Environment in Singapore"',
	'SIMOC': 'Singapore International Mathematics Olympiad Challenge',
	'SIMOC Math Master Mind': 'Singapore International Mathematics Olympiad Challenge',
	'SIMOC Math Olympiad': 'Singapore International Mathematics Olympiad Challenge',
	'SIMOC Mind Sport': 'Singapore International Mathematics Olympiad Challenge',
	'Singa Global Final': 'International Singapore Mathematics Competition',
	'SMKC': 'Singapore Mathematical Kangaroo Contest',
	'SMOPS by Hwa Chong Institution': 'Singapore Mathematical Olympiad for Primary Schools',
	'Speech Academy Asia': 'Series of Public Speaking',
	'VANDA': 'International Science Competition',
	'VANDA Global Finals': 'International Science Competition',
	'VANDA Global Final Team': 'International Science Competition',
	'VANDA Global Final Individual': 'International Science Competition',
	'VTMO': 'Vietnam Titan Mathematical Olympiad',
	'YALA': 'Young Achievers Learning Academy',
	'YALA CSP': 'Young Achievers Learning Academy Community Support Project',
	'YALA Scholarship': 'Young Achievers Learning Academy',
}
achievements = [
	{
		'year': '2022',
		'grade': 'Primary 6',
		'fulfilments': [
			{'title': 'RIPMWC by Raffles Institution', 'award': 'DISTINCTION', 'ranking': 'Top 3% (97.45 percentile, Achievement Score 49%)', 'filename': '2022RIPMWC.pdf'},
			{'title': 'Singa Global Final', 'award': 'GOLD', 'ranking': '', 'filename': '2022SINGA.pdf'},
			{'title': 'BEBRAS', 'award': 'GOLD', 'ranking': '1st in Singapore', 'filename': '2022BEBRAS.pdf'},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': '', 'filename': '2022SMKC.pdf'},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': ''},
		]
	},
	{
		'year': '2021',
		'grade': 'Primary 5',
		'fulfilments': [
			{'title': 'RIPMWC by Raffles Institution', 'award': 'HIGH DISTINCTION', 'ranking': 'estimated due to pandemic, 98 percentile, Achievement Score 50%', 'filename': '2021RIPMWC.jpg'},
			{'title': 'NMOS by NUS High School', 'award': 'SILVER', 'ranking': '', 'filename': '2021NMOS.jpg'},
			{'title': 'SMOPS by Hwa Chong Institution', 'award': 'SILVER', 'ranking': '', 'filename': '2021SMOPS.jpg'},
			{'title': 'Kumon ASHR Mathematics', 'award': '5 Years Ahead', 'ranking': '', 'filename': '2021KUMON.jpg'},
			{'title': 'SIMOC Math Olympiad', 'award': 'GOLD', 'ranking': '', 'filename': '2021SIMOC.pdf'},
			{'title': 'IJMO', 'award': 'GOLD', 'ranking': '', 'filename': ''},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': '2021SASMO.jpg'},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': '', 'filename': '2021SMKC.pdf'},
			{'title': 'DrCT Global Finals', 'award': 'GOLD', 'ranking': '1st Globally', 'filename': ''},
			{'title': 'DrCT', 'award': 'GOLD', 'ranking': '1st in Singapore and 2nd Globally', 'filename': '2021DrCT.pdf'},
			{'title': 'VANDA', 'award': 'SILVER', 'ranking': '', 'filename': '2021VANDA.pdf'},
			{'title': 'VANDA Global Final Individual', 'award': 'BRONZE', 'ranking': '', 'filename': ''},
			{'title': 'VANDA Global Final Team', 'award': 'BRONZE', 'ranking': '', 'filename': ''},
			{'title': 'AMC', 'award': 'DISTINCTION', 'ranking': '', 'filename': '2021AMC.pdf'},
			{'title': 'AMO', 'award': 'SILVER', 'ranking': '1 incorrect answer', 'filename': '2021AMO.pdf'},
			{'title': 'DOKA', 'award': 'DISTINCTION', 'ranking': '', 'filename': '2021DOKA.pdf'},
			{'title': 'YALA CSP', 'award': 'GOLD', 'ranking': '1st place', 'filename': '2021YALACSP.pdf'},
			{'title': 'YALA', 'award': 'Active Participation', 'ranking': '', 'filename': '2021YALA.pdf'},
		]
	},
	{
		'year': '2020',
		'grade': 'Primary 4',
		'fulfilments': [
			{'title': 'SMKC', 'award': 'Perfect Score', 'ranking': '', 'filename': '2020SMKC.jpg'},
			{'title': 'DOKA', 'award': 'HIGH DISTINCTION', 'ranking': '', 'filename': '2020DOKA.jpg'},
			{'title': 'AMC', 'award': 'DISTINCTION', 'ranking': '', 'filename': '2020AMC.jpg'},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': '2020SASMO.jpg'},
			{'title': 'SIMOC Mind Sports', 'award': 'GOLD', 'ranking': '', 'filename': ''},
			{'title': 'SIMOC Math Olympiad', 'award': 'BRONZE', 'ranking': '', 'filename': '2020SIMOC.jpg'},
			{'title': 'SIMOC Math Master Mind', 'award': 'BRONZE', 'ranking': '', 'filename': ''},
			{'title': 'DrCT', 'award': 'SILVER', 'ranking': '', 'filename': '2020DrCT.jpg'},
			{'title': 'AMO', 'award': 'SILVER', 'ranking': '', 'filename': '2020AMO.jpg'},
			{'title': 'VANDA', 'award': 'BRONZE', 'ranking': '', 'filename': '2020VANDA.jpg'},
			{'title': 'VTMO', 'award': 'BRONZE', 'ranking': '', 'filename': '2020VTMO.jpg'},
			{'title': 'Kumon ASHR English', 'award': '3 Years Ahead', 'ranking': '', 'filename': '2020KUMON.jpg'},
		]
	},
	{
		'year': '2019',
		'grade': 'Primary 3',
		'fulfilments': [
			{'title': 'YALA Scholarship', 'award': 'Platinum', 'ranking': '', 'filename': ''},
			{'title': 'SEF', 'award': 'GOLD', 'ranking': '1st', 'filename': '2019SEF.jpg'},
			{'title': 'BEBRAS', 'award': 'GOLD', 'ranking': '2nd in Singapore', 'filename': '2019BEBRAS.jpg'},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': '2019SASMO.jpg'},
			{'title': 'SIMOC', 'award': 'GOLD', 'ranking': '', 'filename': '2019SIMOC.jpg'},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': '', 'filename': '2019SMKC.jpg'},
			{'title': 'AMO', 'award': 'GOLD', 'ranking': '', 'filename': '2019AMO.jpg'},
			{'title': 'AMC', 'award': 'DISTINCTION', 'ranking': '', 'filename': '2019AMC.jpg'},
			{'title': 'ICAS Science', 'award': 'DISTINCTION', 'ranking': '', 'filename': ''},
			{'title': 'iOS App Development with Swift Essential', 'award': 'Accomplishment', 'ranking': '', 'filename': 'iOS.jpg'},
		]
	},
	{
		'year': '2018',
		'grade': 'Primary 2',
		'fulfilments': [
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': '2018SASMO.jpg'},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': '', 'filename': '2018SMKC.jpg'},
			{'title': 'SIMOC', 'award': 'SILVER', 'ranking': '', 'filename': '2018SIMOC.jpg'},
			{'title': 'AMO', 'award': 'SILVER', 'ranking': '', 'filename': '2018AMO.jpg'},
			{'title': 'Speech Academy Asia', 'award': 'Level 1', 'ranking': '', 'filename': ''},
		]
	}
]
learnt_algorithms = [
	{'name':'Floyd Warshall Algorithm', 'id':'floyd-warshall-algorithm'},
	{'name':'Bellman Ford Algorithm', 'id':'bellman-ford-algorithm'},
	{'name':'Minimum Spanning Tree', 'id':'minimum-spanning-tree'},
	{'name':'Breadth First Search', 'id':'breadth-first-search'},
	{'name':'Dynamic Programming', 'id':'dynamic-programming'},
	{'name':'Disjoint Union Set', 'id':'disjoint-union-set'},
	{'name':'Depth First Search', 'id':'depth-first-search'},
	{'name':'Insertion Sort', 'id':'insertion-sort'},
	{'name':'Binary Search', 'id':'binary-search'},
	{'name':'Segment Tree', 'id':'segment-tree'},
	{'name':'Bubble Sort', 'id':'bubble-sort'},
	{'name':'Dijkstra', 'id':'dijkstra'},
]

@app.route('/')
def main_page():
  	return render_template('index.html', contests=contests, achievements=achievements)

@app.route('/family')
def main_page_family():
	return render_template('family.html', title='Family')

@app.route('/family/<name>')
def family_page(name):
	if (name == 'ainunnajib'):
		return render_template('ainunnajib.html', title='Ainun Najib')
	elif (name == 'dzinnun'):
		return render_template('dzinnun.html', title='Ahmad Dzinnun')
	elif (name == 'aisyah'):
		return render_template('aisyah.html', title='Aisyah Atqona Amalia')
	return redirect('/family')

@app.route('/games')
def games():
	return render_template('games.html', title='Games', isDark=False)

@app.route('/algorithms')
def algorithms():
	return render_template('algorithms.html', title='Algorithms', learnt_algorithms=learnt_algorithms)

if __name__ == "__main__":
  	app.run(debug=True, host='0.0.0.0', port=9090)