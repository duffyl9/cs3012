from github import Github

if __name__ == '__main__':
    #Create github account using access token
    g = Github("cf5c737342d428ad6e77d0697e767cf424bb9eaa")
    user = g.get_user("phadej")


#Function for calculating most common langugae used in total repositories
def countLanguages():
    counter = 0
    mostCommon = 0
    commonLanguage = ""

    for repos in g.get_user("phadej").get_repos():
    	for languages in repos.get_languages():
    		currLanguage = languages
    		for repo in g.get_user("phadej").get_repos():
    			for language in repo.get_languages():
    				if currLanguage in language:
    					counter+=1
    		if mostCommon < counter:
    			mostCommon = counter
    			commonLanguage = currLanguage
    		counter=0
    	output = "Most Common Langauage: %s, Number of times used: %s" % (commonLanguage, mostCommon) 
    return output


print(countLanguages())