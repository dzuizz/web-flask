from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

contests = {
	'RIPMWC by Raffles Institution': 'Raffles Institution Primary Mathematics World Contest',
	'SMOPS by Hwa Chong Institution': 'Singapore Mathematical Olympiad for Primary Schools',
	'iOS App Development with Swift Essential': 'InfoTech',
	'Kumon ASHR Mathematics': 'Advanced Student Honour Roll',
	'Speech Academy Asia': '10 Years Series of Public Speaking',
	'Kumon ASHR English': 'Advanced Student Honour Roll',
	'VANDA Global Finals': 'International Science Competition',
	'DrCT Global Finals': 'Doctor Of Computational Thinking',
	'YALA Scholarship': 'Young Achievers Learning Academy',
	'ICAS Science': 'A Science Contest',
	'BEBRAS': 'International Challenge on Informatics and Computational Thinking',
	'SASMO': 'Singapore and Asian Schools Mathematical Olympiad',
	'SIMOC': 'Singapore International Mathematics Olympiad Challenge',
	'VANDA': 'International Science Competition',
	'NMOS by NUS High School': 'National Mathematical Olympiad of Singapore',
	'SMKC': 'Singapore Mathematical Kangaroo Contest',
	'DrCT': 'Doctor Of Computational Thinking',
	'DOKA': 'Depth Of Knowledge Assesment',
	'VTMO': 'Vietnam Titan Mathematical Olympiad',
	'IJMO': 'International Junior Mathematical Olympiad',
	'AMO': 'American Mathematics Olympiad',
	'AMC': 'Australian Mathematics Olympiad',
	'SEF': 'Scholastic Environmental Fund - theme: "Youth Taking Action to Prevent Negative Impact on Non-Human Environment in Singapore"',
}
achievements = [
	{
		'year': '2022',
		'grade': 'Primary 6',
		'fulfilments': [
			{'title': 'RIPMWC by Raffles Institution', 'award': '49%', 'ranking': 'Top 3% (97.45 percentile)', 'filename': ''},
			{'title': 'BEBRAS', 'award': 'GOLD', 'ranking': '1st in Singapore', 'filename': ''},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': ''},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': '', 'filename': ''},
		]
	},
	{
		'year': '2021',
		'grade': 'Primary 5',
		'fulfilments': [
			{'title': 'DrCT Global Finals', 'award': 'GOLD', 'ranking': '1st Globally', 'filename': ''},
			{'title': 'DrCT', 'award': 'GOLD', 'ranking': '1st in Singapore and 2nd Globally', 'filename': ''},
			{'title': 'IJMO', 'award': 'GOLD', 'ranking': '', 'filename': ''},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': '2021SASMO.jpg'},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': '', 'filename': ''},
			{'title': 'NMOS by NUS High School', 'award': 'SILVER', 'ranking': '', 'filename': '2021NMOS.jpg'},
			{'title': 'RIPMWC by Raffles Institution', 'award': '50%', 'ranking': '', 'filename': '2021RIPMWC.jpg'},
			{'title': 'SMOPS by Hwa Chong Institution', 'award': 'SILVER', 'ranking': '', 'filename': '2021SMOPS.jpg'},
			{'title': 'VANDA', 'award': 'SILVER', 'ranking': '', 'filename': ''},
			{'title': 'Kumon ASHR Mathematics', 'award': '5 Years Ahead', 'ranking': '', 'filename': '2021KUMON.jpg'},
		]
	},
	{
		'year': '2020',
		'grade': 'Primary 4',
		'fulfilments': [
			{'title': 'SMKC', 'award': 'Perfect Score', 'ranking': '', 'filename': '2020SMKC.jpg'},
			{'title': 'DOKA', 'award': 'HIGH DISTINCTION', 'ranking': '', 'filename': '2020DOKA.jpg'},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': '', 'filename': '2020SASMO.jpg'},
			{'title': 'SIMOC', 'award': 'GOLD', 'ranking': '', 'filename': '2020SIMOC.jpg'},
			{'title': 'DrCT', 'award': 'SILVER', 'ranking': '', 'filename': '2020DrCT.jpg'},
			{'title': 'AMC', 'award': 'DISTINCTION', 'ranking': '', 'filename': '2020AMC.jpg'},
			{'title': 'AMO', 'award': 'SILVER', 'ranking': '', 'filename': '2020AMO.jpg'},
			{'title': 'VANDA Global Finals', 'award': 'BRONZE', 'ranking': '', 'filename': '2020VANDA.jpg'},
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
	{'name':'Binary Search', 'id':'binary-search'},
	{'name':'Disjoint Union Set', 'id':'disjoint-union-set'},
	{'name':'Segment Tree', 'id':'segment-tree'},
	{'name':'Dynamic Programming', 'id':'dynamic-programming'},
	{'name':'Bubble Sort', 'id':'bubble-sort'},
	{'name':'Minimum Spanning Tree', 'id':'minimum-spanning-tree'},
	{'name':'Depth First Search', 'id':'depth-first-search'},
	{'name':'Breadth First Search', 'id':'breadth-first-search'},
	{'name':'Dijkstra', 'id':'dijkstra'},
	{'name':'Insertion Sort', 'id':'insertion-sort'},
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