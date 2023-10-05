import PyPDF2
from rake_nltk import Rake

#creates array to store text from pdf 
def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        #pdf_text = []
        text = open("text.txt", "w")

        for page in reader.pages:
            content = page.extract_text()
            #pdf_text.append(content)
            text.write(content)
        text.close()
        #text = pdf_text[0]  
        
    #clean_data()
    rake()  
   
def rake():
    text = open("text.txt", "r")
    input_text = text.read()
    r = Rake(punctuations=['.','`','/','\'','~','-','=','"',',',':',';','+','.,',',.',
                           '(',')','[',']','{','}',').','),','].','],','}.','}.','~/','/~',
                           '1','2','3','4','5','6','7','8','9','0',
                           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    
    r.extract_keywords_from_text(input_text)
    #keywords = r.get_ranked_phrases()
    #print (set([keyword for keyword in keywords if len(keyword.split()) > 0]))
    ranked = r.get_word_frequency_distribution()
    most_occured_numbers = []
    most_occured_words = []
    key_value = []
    top10 = []
    for k,v in ranked.items():
        #most_occured_numbers = ranked.i
        if v > 10:
            most_occured_numbers.append(v)
            #most_occured_words = most_occured_words.append(k)
            most_occured_words.append(k)
            key_value.append([v,k])
        key_value.sort()
        key_value.reverse()
    i = 0
    for k,v in key_value:
        while i < 10:
            top10.append(key_value.pop(0))
            if i!=10:
                i = i+1
            else:
                break
    top10_most_occured_words = []
    for k,v in top10:
        top10_most_occured_words.append(v)
    

    
    #print (most_occured_numbers)
    #print (most_occured_words)
    #print (key_value)
    #print (top10)
    print (top10_most_occured_words)
    '''    if v > 5:
            most_occured_numbers.append(v)
    most_occured_numbers.sort()
    most_occured_numbers.reverse()
    most_occured = []
    most_occured = most_occured.append(most_occured_numbers.pop(0))

    print(most_occured)
    #if (most_occured_numbers.__contains__(1)):
        #print("true")

'''

  #  for rank in ranked:
  #          temp = ranked.popitem()
  #          if temp.values() > 3:
  #              most_occured = most_occured.append(temp.key())
  #      
  #          most_occured = most_occured.append(ranked.values())

    #most_occured.sort()
    #most_occured.reverse()
    #print(most_occured_numbers)
        

    #print (ranked.keys())#.__reduce__)
    #.pop("",10)) #(set([rank for rank in ranked if len(ranked) < 10]))
    
     

'''def clean_data():
    text = open("text.txt", "r")
    input_text = text.read()
    input_text = input_text.replace("(","").replace(")","").replace("[","").replace("]","").replace("{","").replace("}","").replace(".","").replace("~","").replace("/","").replace("\"","").replace("-","")
    input_text = input_text.replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","")
    input_text = input_text.replace("et al","")
    rake(input_text)
'''

if __name__ == '__main__':
    extracted_text = extract_text_from_pdf('sample.pdf')
    keyword_count = 0
    #print(r.get_ranked_phrases_with_scores())
   
   
   
   
   
   
   
   
   
   
   
   
   
    '''for text in extracted_text:
        split_message = re.split(r'\s+|[,;?.-]\s*', text.lower())

        if 'zero' in split_message:
            keyword_count += 1

        #extract_keywords_from_text(extracted_text)
        print("Keyword Found: ", keyword_count, "instances")
'''