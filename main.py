import bs4, requests
from datetime import date

def getFootballTable(url, dateOfResults):
    data = []
    table = []
    scores = []
    myDate = date.today().strftime("%d/%m/%y")
    specificDate = False

    if(len(dateOfResults) == 0 or len(dateOfResults) == 8):
        specificDate = True
        if(len(dateOfResults) == 8):
            myDate = dateOfResults

    # Get the latest scores from the website
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table', attrs={'title':'Results Table'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    # Convert that beautifulSoup into a lovely tidy broth
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

    # Convert the sentence into a pretty form
    for results in data:
        sentence = ''
        # We only want todays results get rid of the old ones
        if(len(results)> 0):
            if(specificDate):
                if(results[1][:8] == myDate):
                    sentence = '  '.join(results)
                    scores.append(sentence)
            else:
                sentence = '  '.join(results)
                scores.append(sentence)

    # make it prettier if no results for today yet
    if(len(scores) == 0 ):
        scores = ["No Results yet"]

    return '\n'.join(scores)

def getLeagueResults(league, dateOfResults):
    teams = ['http://fulltime-league.thefa.com/ListPublicResult.do?selectedFixtureGroupKey=1_650520015&selectedRelatedFixtureOption=2&selectedClub=&selectedTeam=&selectedDateCode=all&selectednavpage1=1&navPageNumber1=1&previousSelectedFixtureGroupKey=1_668764192&previousSelectedFixtureGroupAgeGroup=0&previousSelectedClub=850066899&seasonID=499196596&selectedSeason=499196596',
            'http://fulltime-league.thefa.com/ListPublicResult.do?selectedFixtureGroupKey=1_668764192&selectedRelatedFixtureOption=2&selectedClub=&selectedTeam=&selectedDateCode=all&selectednavpage1=1&navPageNumber1=1&previousSelectedFixtureGroupKey=1_336078148&previousSelectedFixtureGroupAgeGroup=0&previousSelectedClub=850066899&seasonID=499196596&selectedSeason=499196596',
            'http://fulltime-league.thefa.com/ListPublicResult.do?selectedFixtureGroupKey=1_203505173&selectedRelatedFixtureOption=2&selectedClub=&selectedTeam=&selectedDateCode=all&selectednavpage1=1&navPageNumber1=1&previousSelectedFixtureGroupKey=1_477651683&previousSelectedFixtureGroupAgeGroup=0&previousSelectedClub=850066899&seasonID=499196596&selectedSeason=499196596',
            'http://fulltime-league.thefa.com/ListPublicResult.do?selectedFixtureGroupKey=1_666860982&selectedRelatedFixtureOption=2&selectedClub=&selectedTeam=&selectedDateCode=all&selectednavpage1=1&navPageNumber1=1&previousSelectedFixtureGroupKey=1_477651683&previousSelectedFixtureGroupAgeGroup=0&previousSelectedClub=850066899&seasonID=499196596&selectedSeason=499196596',
            'http://fulltime-league.thefa.com/ListPublicResult.do?selectedFixtureGroupKey=1_477651683&selectedRelatedFixtureOption=2&selectedClub=&selectedTeam=&selectedDateCode=all&selectednavpage1=1&navPageNumber1=1&previousSelectedFixtureGroupKey=1_666860982&previousSelectedFixtureGroupAgeGroup=0&previousSelectedClub=850066899&seasonID=499196596&selectedSeason=499196596',
            'http://fulltime-league.thefa.com/ListPublicResult.do?selectedFixtureGroupKey=1_293246458&selectedRelatedFixtureOption=2&selectedClub=&selectedTeam=&selectedDateCode=all&selectednavpage1=1&navPageNumber1=1&previousSelectedFixtureGroupKey=1_293246458&previousSelectedFixtureGroupAgeGroup=0&previousSelectedClub=850066899&seasonID=499196596&selectedSeason=499196596']
    allBoroughUrl = 'http://fulltime-league.thefa.com/ListPublicResult.do?selectedFixtureGroupKey=&selectedRelatedFixtureOption=2&selectedClub=850066899&selectedTeam=&selectedDateCode=all&selectednavpage1=1&navPageNumber1=1&previousSelectedFixtureGroupKey=&previousSelectedFixtureGroupAgeGroup=0&previousSelectedClub=850066899&seasonID=499196596&selectedSeason=499196596'

    if(league and int(league)<= 6 and int(league)>0):
        results = getFootballTable(teams[int(league)-1], dateOfResults)
    else:
        results = getFootballTable(allBoroughUrl, dateOfResults)

    print(results)

dateOfResults = input('Not todays results?:\nall /Specific date(dd/mm/yy)\n')
league = input('Which Team would you like results for? \nLeave blank for all teams \n')

getLeagueResults(league, dateOfResults)
