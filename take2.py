import time
import pandas as pd
import urllib2  

from bs4 import BeautifulSoup 

#Ratings
def get_ratings1(linktourl):
    
    rating=0
    divTag = soup.find_all("div", {"class": "search-item-info"})
    counter=0

    #you do not have any ratings, please proceed to next URL
    for tag in divTag:    
        tdTags = tag.find_all("span", {"class": "star-rating star-rating-empty"})  
        if(len(tdTags)==1):
            counter=counter+1

    #this is when you have ratings,get ratings
    if(counter==0):
       
        minicounter=-1
        for tag in divTag:
            minicounter=minicounter+1
            if(minicounter==1):
                tag2 = tag.find_all("span", {"class": "star-rating"})
                for minitag2 in tag2:
                    rating=minitag2.get('title')
                    
    #get this rating  
    #print rating
    return rating
#-------------------------------------------------------2----------------------
def get_ratings(linktourl,soup_incoming):
    rating=0
    divTag = soup_incoming.find_all("div", {"class": "search-item-info"})
    counter=0

    #you do not have any ratings, please proceed to next URL
    for tag in divTag:    
        tdTags = tag.find_all("span", {"class": "star-rating star-rating-empty"})  
        if(len(tdTags)==1):
            counter=counter+1

    #this is when you have ratings,get ratings
    if(counter==0):
        
        minicounter=-1
        for tag in divTag:
            minicounter=minicounter+1
            if(minicounter==1):
                tag2 = tag.find_all("span", {"class": "star-rating"})
                for minitag2 in tag2:
                    rating=minitag2.get('title')

    #get this rating  
    #print rating
    return rating




def get_badges1(linktourl):
    rating=0
    badges_returned = soup.find_all("div",attrs={"class": "badges"})
    if(len(badges_returned)!=0):
        badges=True
    else:
        badges=False
    return badges

#-------------------------------------------------------2----------------------
def get_badges(linktourl,soup_incoming):
    rating=0
    badges_returned = soup_incoming.find_all("div",attrs={"class": "badges"})
    if(len(badges_returned)!=0):
        badges=True
    else:
        badges=False
    return badges


def get_comments1(linktourl):
    total_comments=0
    comments=[]
    comments_returned = soup.find_all("p",attrs={"itemprop": "reviewBody"})
    
    for comm in comments_returned:
        comments.append(comm.getText())
    total_comments= len(comments)
    return comments    
#-------------------------------------------------------2----------------------
def get_comments(linktourl,soup_incoming):
    total_comments=0
    comments=[]
    date_list=[]
    comments_returned = soup_incoming.find_all("p",attrs={"itemprop": "reviewBody"})
    
    for comm in comments_returned:
        comments.append(comm.getText())
    total_comments= len(comments)
    #change1
    comments_date= soup.find_all("a",attrs={"class": "link-plain"})
    for d in comments_date:
        date_text=str(d.getText())
        date_text=date_text.replace("Submitted","")
        date_text=date_text.strip()
        dt = parser.parse(date_text)
        date_final=str(dt.date())
        date_list.append(date_final)

    
    return zip(comments,date_list) 

    #change2
    #return comments    


def get_values_reviews1(linktourl):

    val_returned = soup.find_all("span",attrs={"class": "value"})
    valcounter=0
    random_list=[]
    main_val=[]
    dny_list=[]
    
    for val in val_returned:
        random_list.append(val.getText())
    dnycnt=0
    for val in random_list:
        dny_list.append(val)
        dnycnt=dnycnt+1
        if(dnycnt==4):
            main_val.append(dny_list)
            dny_list=[]
            dnycnt=0
    
      
    comments_final=get_comments1(linktourl) 
    
    #([(5,5,5,5),'review 1'],[(5,5,5,5),'review 1'])     
    return zip(main_val,comments_final)
#-------------------------------------------------------2----------------------
def get_values_reviews(linktourl,soup_incoming):

    val_returned = soup_incoming.find_all("span",attrs={"class": "value"})
    valcounter=0
    random_list=[]
    main_val=[]
    dny_list=[]
    
    for val in val_returned:
        random_list.append(val.getText())
    dnycnt=0
    for val in random_list:
        dny_list.append(val)
        dnycnt=dnycnt+1
        if(dnycnt==4):
            main_val.append(dny_list)
            dny_list=[]
            dnycnt=0
    
      
    comments_final=get_comments(linktourl,soup_incoming) 
    
    #([(5,5,5,5),'review 1'],[(5,5,5,5),'review 1'])     
    return zip(main_val,comments_final)


#Num of reviews

def get_reviws1(linktourl):
    #print 'get_ratings started'
    rating=0
    divTag = soup.find_all("div", {"class": "search-item-info"})
    counter=0

    #you do not have any ratings, please proceed to next URL
    for tag in divTag:    
        tdTags = tag.find_all("span", {"class": "star-rating star-rating-empty"})  
        if(len(tdTags)==1):
            counter=counter+1

    #this is when you have ratings,get ratings
    if(counter==0):
        #print'there exists rating'
        minicounter=-1
        for tag in divTag:
            minicounter=minicounter+1
            if(minicounter==1):
                tag2 = tag.find_all("span", {"class": "star-rating"})
                for minitag2 in tag2:
                    rating=minitag2.get('title')
                    #print minitag2.get('title')

    #get this rating  
    #print rating
    return rating
#-------------------------------------------------------2----------------------
def get_reviws(linktourl,soup_incoming):
    #print 'get_ratings started'
    revs = soup.find('div', attrs={'class': 'star-rating-count'})
    if revs is None:
        execute(quote_page,0,name_incoming)
    else:
        revs = soup.find('div', attrs={'class': 'star-rating-count'})
        for rev in revs:
            ans=str(rev.getText())
            num_of_rev=int(ans)
            break
    return num_of_rev




def get_name(linktourl,soup_incoming):
    name_box = soup_incoming.find('div', attrs={'class': 'col-sm-6'}).h1 
    if name_box is None:
        name='N/A'
    else:
        name = name_box.text.strip()
    
    return name

def begin_not_begin(quote_page,name_incoming,npi_incoming):
    revs = soup.find('div', attrs={'class': 'star-rating-count'})
    if revs is None:
        execute(quote_page,0,name_incoming,npi_incoming)
    else:
        revs = soup.find('div', attrs={'class': 'star-rating-count'})
        for rev in revs:
            ans=str(rev.getText())
            num_of_rev=int(ans)
            break
        if(num_of_rev!=0):
        #get new url to visit
            link1=soup.find('a', attrs={'class': 'search-item-doctor-link'})
            link2=link1['href'].encode('utf-8')
            url_new='https://www.ratemds.com'+link2
            execute(url_new,1,name_incoming,npi_incoming)       

def report_error(name_incoming,npi_incoming):
    error_list_name.append(name_incoming,npi_incoming)
    
def execute(url,param,name_incoming,npi_incoming):

    if(param==1):
        quote_page2 =  url
        
        hdr = {'User-Agent': 'Mozilla/5.0'}
        try:
            req = urllib2.Request(quote_page2,headers=hdr)
            time.sleep(5)
            page = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            error_message = e.read()
            error_list.append(quote_page)
            print error_message
            report_error(name_incoming,npi_incoming)
        
        
        soup_new = BeautifulSoup(page)
        
        name=get_name(quote_page2,soup_new)
        num_reviews=get_reviws(quote_page2,soup_new)
        rating_final=get_ratings(quote_page2,soup_new)
        badges_final=get_badges(quote_page2,soup_new)
        comments_final=len(get_comments(quote_page2,soup_new))
        val_review=get_values_reviews(quote_page2,soup_new)
        data1.append((npi_incoming,name,num_reviews,rating_final,badges_final,comments_final,val_review))
    
    else:
        name_final=name_incoming.replace("%20"," ")
        num_reviews=get_reviws1(url)
        rating_final=get_ratings1(url)
        badges_final=get_badges1(url)
        comments_final=get_comments1(url)
        
        val_review=get_values_reviews1(url)
        data1.append((npi_incoming,name_final,num_reviews,rating_final,badges_final,comments_final,val_review))

def get_name_from_csv_string(name_incoming):
    name2=name.replace("%20"," ")
    return name2
    
df = pd.read_csv('/Users/dny/Desktop/sarkar/Prof2Submit/main.csv',usecols=["NPI", "DnyName"])
col = df['DnyName']
thiscounter=0
data1=[]
error_list_url=[]
error_list_name=[]
base='_____________URL HERE______________'
for npi,name_loop in df.itertuples(index=False):
    thiscounter=thiscounter+1
            
    quote_page =  base+name_loop
    
    if(thiscounter%25==0):
        print thiscounter
        print quote_page
    
    
    
    
    hdr = {'User-Agent': 'Mozilla/5.0'}
    try:
        req = urllib2.Request(quote_page,headers=hdr)
        time.sleep(5)
        page = urllib2.urlopen(req)
    
    except urllib2.HTTPError as e:
        error_message = e.read()
        error_list.append(quote_page)
   
        error_list_name.append(npi)

    
    
    soup = BeautifulSoup(page)
    num_of_rev=0
    begin_not_begin(quote_page,name_loop,npi)    
    
print len(data1)
        