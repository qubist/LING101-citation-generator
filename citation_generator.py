file = open("data.txt","r")

data = file.read().splitlines()

# print(data)

for dataString in data:
    author = dataString.split("; ")[0]
    title = dataString.split("; ")[1]
    # print(f'Author: {author}')
    # print(f'title: {title}')
    lastName = ' '.join(author.split()[1:])
    firstName = str(author.split()[0])

# lastName = "Harris-Braun"
# firstName = "Will"
# paperTitle = "Outside the Lines"

    citation = f"{lastName}, {firstName}. 2019. \"{title}.\" Paper submitted for Linguistics 101: Introduction to Linguistics. Haverford College, Spring 2019; Prof. B. Lillehaugen.\n"

    print(citation)
