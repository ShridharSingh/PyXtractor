import PyPDF2
from rake_nltk import Rake
import json

#creates array to store text from pdf 
def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        text = open("text.txt", "w")

        for page in reader.pages:
            content = page.extract_text()
            text.write(content)
        text.close()

    rake()  
   
def rake():
    text = open("text.txt", "r")
    input_text = text.read()

    #remove anomalies from text
    r = Rake(punctuations=['.','`','/','\'','~','-','=','"',',',':',';','+','.,',',.',
                           '(',')','[',']','{','}',').','),','].','],','}.','}.','~/','/~',
                           '1','2','3','4','5','6','7','8','9','0',
                           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    
    r.extract_keywords_from_text(input_text)
    ranked = r.get_word_frequency_distribution()
   
    #Sorting Arrays 
    most_occured_numbers = []
    most_occured_words = []
    key_value = []
    top10 = []
    top10_most_occured_words = []
    
    #Iterable Variables
    iterable = 0

    for k,v in ranked.items():
        if v > 10:
            most_occured_numbers.append(v)
            most_occured_words.append(k)
            key_value.append([v,k])
        key_value.sort()
        key_value.reverse()
    
    for k,v in key_value:
        while iterable < 10:
            top10.append(key_value.pop(0))
            if iterable!=10:
                iterable = iterable+1
            else:
                break

    for k,v in top10:
        top10_most_occured_words.append(v)
    
    #print or export to json : print(top10_most_occured_words)
    export_to_json(top10_most_occured_words)

def export_to_json(top10_input_array):
    
    dictonary = {
        "keyword0":top10_input_array[0],
        "keyword1":top10_input_array[1],
        "keyword2":top10_input_array[2],
        "keyword3":top10_input_array[3],
        "keyword4":top10_input_array[4],
        "keyword5":top10_input_array[5],
        "keyword6":top10_input_array[6],
        "keyword7":top10_input_array[7],
        "keyword8":top10_input_array[8],
        "keyword9":top10_input_array[9],
    }
    json_object = json.dumps(dictonary, indent=10)
    with open("input.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    pdfname = input("Enter name of pdf you want to extract keywords from: ")
    extracted_text = extract_text_from_pdf(pdfname)