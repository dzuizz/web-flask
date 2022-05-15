from re import S
from flask import Flask, render_template, url_for
#from flask_sqlalchemy import SQLAlchemy
#Azure App Service doesn't support Flask_SQLAlchemy

app = Flask(__name__)

contests = {
	'iOS App Development with Swift Essential': 'InfoTech',
	'Kumon ASHR Mathematics': 'Advanced Student Honour Roll',
	'Speech Academy Asia': '10 Years Series of Public Speaking',
	'Kumon ASHR English': 'Advanced Student Honour Roll',
	'Vanda Global Finals': 'A Science Olympiad',
	'DrCT Global Finals': 'Doctor Of Computational Thinking',
	'YALA Scholarship': 'Young Achievers Learning Academy',
	'ICAS Science': 'A Science Contest',
	'RIPMWC': 'Raffles Instituition Primary Mathematics World Contest',
	'BEBRAS': 'Lithuanian word for "beaver"',
	'SMOPS': 'Singapore Mathematical Olympiad for Primary Schools',
	'SASMO': 'Singapore and Asian Schools Mathematical Olympiad',
	'SIMOC': 'Singapore International Mathematics Olympiad Challenge',
	'Vanda': 'A Scince Olympiad',
	'NMOS': 'National Mathematical Olympiad of Singapore',
	'SMKC': 'Singapore Mathematical Kangaroo Contest',
	'DrCT': 'Doctor Of Computational Thinking',
	'DOKA': 'Depth Of Knowledge Assesment',
	'VTMO': 'Vietnam Titan Mathematical Olympiad',
	'IJMO': 'International Junior Mathematical Olympiad',
	'AMO': 'American Mathematics Olympiad',
	'AMC': 'Australian Mathematics Olympiad',
	'SEF': 'Scholastic Environmental Fund',
}
achievements = [
	{
		'year': '2022',
		'fulfilments': [
			{'title': 'RIPMWC', 'award': '49%', 'ranking': 'Top 3% (97.45 percentile)'},
			{'title': 'BEBRAS', 'award': 'GOLD', 'ranking': '1st in Singapore'},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': ''},
		]
	},
	{
		'year': '2021',
		'fulfilments': [
			{'title': 'DrCT Global Finals', 'award': 'GOLD', 'ranking': '1st Globally'},
			{'title': 'DrCT', 'award': 'GOLD', 'ranking': '1st in Singapore and 2nd Globally'},
			{'title': 'IJMO', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': ''},
			{'title': 'NMOS', 'award': 'SILVER', 'ranking': ''},
			{'title': 'RIPMWC', 'award': '50%', 'ranking': ''},
			{'title': 'SMOPS', 'award': 'SILVER', 'ranking': ''},
			{'title': 'Kumon ASHR Mathematics', 'award': '5 Years Ahead', 'ranking': ''}
		]
	},
	{
		'year': '2020',
		'fulfilments': [
			{'title': 'SMKC', 'award': 'Perfect Score', 'ranking': ''},
			{'title': 'DOKA', 'award': 'HIGH DISTINCTION', 'ranking': ''},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SIMOC', 'award': 'GOLD', 'ranking': ''},
			{'title': 'DrCT', 'award': 'SILVER', 'ranking': ''},
			{'title': 'AMC', 'award': 'DISTINCTION', 'ranking': ''},
			{'title': 'AMO', 'award': 'SILVER', 'ranking': ''},
			{'title': 'Vanda Global Finals', 'award': 'BRONZE', 'ranking': ''},
			{'title': 'VTMO', 'award': 'BRONZE', 'ranking': ''},
			{'title': 'Kumon ASHR English', 'award': '3 Years Ahead', 'ranking': ''},
		]
	},
	{
		'year': '2019',
		'fulfilments': [
			{'title': 'YALA Scholarship', 'award': 'Platinum', 'ranking': ''},
			{'title': 'SEF', 'award': 'GOLD', 'ranking': '1st'},
			{'title': 'BEBRAS', 'award': 'GOLD', 'ranking': '2nd in Singapore'},
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SIMOC', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': ''},
			{'title': 'AMO', 'award': 'GOLD', 'ranking': ''},
			{'title': 'AMC', 'award': 'DISTINCTION', 'ranking': ''},
			{'title': 'ICAS Science', 'award': 'DISTINCTION', 'ranking': ''},
			{'title': 'iOS App Development with Swift Essential', 'award': 'Accomplishment', 'ranking': ''},
		]
	},
	{
		'year': '2018',
		'fulfilments': [
			{'title': 'SASMO', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SMKC', 'award': 'GOLD', 'ranking': ''},
			{'title': 'SIMOC', 'award': 'SILVER', 'ranking': ''},
			{'title': 'AMO', 'award': 'SILVER', 'ranking': ''},
			{'title': 'Speech Academy Asia', 'award': 'Level 1', 'ranking': ''},
		]
	}
]

@app.route('/')
def main_page():
  	return render_template('index.html', contests=contests, achievements=achievements)

@app.route('/family')
def main_page_family():
	return render_template('family.html', title='Family')

@app.route('/games')
def games():
	return render_template('games.html', title='Games')

if __name__ == "__main__":
  	app.run(debug=True, host='0.0.0.0', port=9090)