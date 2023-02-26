{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 0 \n",
    "def b():\n",
    "    global a\n",
    "    a = c(a)\n",
    "\n",
    "def c(a):\n",
    "    return a + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-8d7b4527e81d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ma\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not callable"
     ]
    }
   ],
   "source": [
    "a()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Function fileLength(), given to you, takes the name of a file as input and returns the length of the file:\n",
    "\n",
    ">>> fileLength('midterm.py') 284\n",
    ">>> fileLength('idterm.py') Traceback (most recent call last):\n",
    "File \"<pyshell#34>\", line 1, in <module> fileLength('idterm.py')\n",
    "File \"/Users/me/midterm.py\", line 3, in fileLength infile = open(filename)\n",
    "FileNotFoundError: [Errno 2] No such file or directory: 'idterm.py'\n",
    "\n",
    "As shown above, if the file cannot be found by the interpreter or if it cannot be read as a text file, an exception will be raised. Modify function fileLength() so that a friendly message is printed instead:\n",
    "\n",
    ">>> fileLength('midterm.py') 358\n",
    ">>> fileLength('idterm.py') File idterm.py not found.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "import os\n",
    "#function to check file length\n",
    "def fileLength(file_name):\n",
    "  try:\n",
    "    length = os.path.getsize(file_name)\n",
    "    return length\n",
    "  except FileNotFoundError:\n",
    "    #return file not found string\n",
    "    return \"File \"+file_name+\" not found.\"\n",
    "#call function to print size\n",
    "print(fileLength(\"test.py\"))   \n",
    "print(fileLength(\"test112233.py\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Question 3\n",
    "Write a class named Marsupial that can be used as shown below:\n",
    "\n",
    ">>> m = Marsupial()\n",
    ">>> m.put_in_pouch('doll')\n",
    ">>> m.put_in_pouch('firetruck')\n",
    ">>> m.put_in_pouch('kitten')\n",
    ">>> m.pouch_contents() ['doll', 'firetruck', 'kitten']\n",
    "Now write a class named Kangaroo as a subclass of Marsupial that inherits all the attributes of Marsupial and also:\n",
    "a.\textends the Marsupial __init__ constructor to take, as input, the\n",
    "coordinates x and y of the Kangaroo object,\n",
    "b.\tsupports method jump that takes number values dx and dy as input and moves the kangaroo by dx units along the x-axis and by dy units along the y- axis, and\n",
    "c.\toverloads the __str__ operator so it behaves as shown below.\n",
    "\n",
    ">>> k = Kangaroo(0,0)\n",
    ">>> print(k)\n",
    "I am a Kangaroo located at coordinates (0,0)\n",
    ">>> k.put_in_pouch('doll')\n",
    ">>> k.put_in_pouch('firetruck')\n",
    ">>> k.put_in_pouch('kitten')\n",
    ">>> k.pouch_contents() ['doll', 'firetruck', 'kitten']\n",
    ">>> k.jump(1,0)\n",
    ">>> k.jump(1,0)\n",
    ">>> k.jump(1,0)\n",
    ">>> print(k)\n",
    "I am a Kangaroo located at coordinates (3,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Marsupial:\n",
    "    def __init__(self):\n",
    "        self.pouch = []\n",
    "    \n",
    "    def put_in_pouch(self, obj):\n",
    "        self.pouch.append(obj)\n",
    "    \n",
    "    def pouch_contents(self):\n",
    "        print(self.pouch)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "m = Marsupial()\n",
    "m.put_in_pouch('doll')\n",
    "m.put_in_pouch('firetruck')\n",
    "m.put_in_pouch('kitten')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.Marsupial object at 0x0000017F8941D880>\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "def main():\n",
    "    collatz(10)\n",
    "\n",
    "def collatz(x):\n",
    "    if x == 1:\n",
    "        print (x)\n",
    "    elif x % 2 == 0:\n",
    "        print (x)\n",
    "        x = x/2\n",
    "        collatz(x)\n",
    "    else:\n",
    "        print (x)\n",
    "        \n",
    "x = 3*x + 1\n",
    "    collatz(x)\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "def binary(n):\n",
    "   if n == 0:\n",
    "       return \"0\"\n",
    "   else:\n",
    "       return binary(n // 2) + str(n % 2)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "from html.parser import HTMLParser\n",
    "#create a subclass of HTMLParser which will overload handle..\n",
    "class HeadingParser(HTMLParser):\n",
    "    headerFlag = False\n",
    "    indent = 0\n",
    "    #Triggered when an opening tag is encountered\n",
    "    def handle_starttag(self, tag, attrs):      \n",
    "        if tag == \"h1\":\n",
    "            #Set flag which says we are in an header\n",
    "            self.headerFlag = True\n",
    "            #Set indent to 0\n",
    "            self.indent= 0\n",
    "        elif tag == \"h2\":\n",
    "            #Set flag which says we are in an header\n",
    "            self.headerFlag = True\n",
    "            #Set indent to 1\n",
    "            self.indent= 1\n",
    "        elif tag == \"h3\":\n",
    "            #Set flag which says we are in an header\n",
    "            self.headerFlag = True\n",
    "            #Set indent to 2\n",
    "            self.indent= 2\n",
    "        elif tag == \"h4\":\n",
    "            #Set flag which says we are in an header\n",
    "            self.headerFlag = True\n",
    "            #Set indent to 3\n",
    "            self.indent= 3\n",
    "        elif tag == \"h5\":\n",
    "            #Set flag which says we are in an header\n",
    "            self.headerFlag = True\n",
    "            #Set indent to 4\n",
    "            self.indent= 4\n",
    "        elif tag == \"h6\":\n",
    "            #Set flag which says we are in an header\n",
    "            self.headerFlag = True\n",
    "            #Set indent to 5\n",
    "            self.indent= 5\n",
    "        else:\n",
    "            #ReSet flag\n",
    "            self.headerFlag = False\n",
    "            #Set indent to 0\n",
    "            self.indent= 0\n",
    "    #Triggered when data found\n",
    "    def handle_data(self, data):                \n",
    "        if self.headerFlag: \n",
    "            space = \" \"*self.indent\n",
    "            print(\"%s%s\" % (space,data))\n",
    "    #Handle end of a tag\n",
    "    def handle_endtag(self, tag):\n",
    "        #ReSet flag\n",
    "        if tag in [\"h1\",\"h2\",\"h3\",\"h4\",\"h5\",\"h6\"]:\n",
    "            self.headerFlag = False\n",
    "\n",
    "\n",
    "hParser = HeadingParser()\n",
    "#Open the file\n",
    "file = open(\"w3c.html\", \"r\")\n",
    "#Read entirely the file         \n",
    "html = file.read()                  \n",
    "#Close the file \n",
    "file.close()    \n",
    "#Parse the file contents                \n",
    "hParser.feed(html)            "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The function should first print the provided link, then get all the links in the provided webpage and iterate throuh them, calling itself for each of the links, changing the parameters so that the function knows the current depth and indent and can test them to kwow when to stop. \n",
    "Step-by-step explanation\n",
    "First, the function to retrieve all the links from a website, using BeautifulSoup:\n",
    "\n",
    "\n",
    "from bs4 import BeautifulSoup, SoupStrainer\n",
    "import httplib2\n",
    "\n",
    "def getLinks(url):\n",
    "    res = []\n",
    "    http = httplib2.Http()\n",
    "    status, response = http.request(url)\n",
    "\n",
    "    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features=\"html.parser\"):\n",
    "        if link.has_attr('href'):\n",
    "            if link['href'][:5] == \"http:\" or link['href'][:5] == \"https\":\n",
    "                res.append(link['href'])\n",
    "    return res\n",
    "\n",
    "This funtion simply finds all the <a> tags in the provided page and gets their corresponding url. \n",
    "Now, the webdir function: \n",
    "def webdir(url, depth, indent):\n",
    "    \n",
    "    print(indent*\" \" + url)\n",
    "\n",
    "    if depth == 0:\n",
    "        return\n",
    "\n",
    "    for i in getLinks(url):\n",
    "        webdir(i, depth-1, indent+1)\n",
    "\n",
    "webdir(\"http://www.nytimes.com/\", 2, 0)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 8"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "a) SELECT temperature from tablename;\n",
    "b) SELECT distinct city from tablename;\n",
    "c) select * from tablename where country='India';\n",
    "d) select * from tablename where season='Fall';\n",
    "e) select city, country, season from tablename where rainfaill >= 200\n",
    "and rainfall <= 400;\n",
    "f) select city, country from tablename where temperature>20\n",
    "order by temperature ASC;\n",
    "g) select count(rainfall) from tablename where city='Cairo';\n",
    "h) select rainfall, count(rainfall) from tablename \n",
    "group by rainfall;\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Question 9"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE', 'LAZY', 'DOG']\n"
     ]
    }
   ],
   "source": [
    "def Upper(words):\n",
    "    for i in range(len(words)):\n",
    "        #convert every word in uppercase\n",
    "        words[i]=words[i].upper()\n",
    "    return words\n",
    "\n",
    "\n",
    "words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n",
    "#call function\n",
    "list_Upper=Upper(words)\n",
    "#print new list\n",
    "print(list_Upper)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n"
     ]
    }
   ],
   "source": [
    "def Lower(words):\n",
    "    for i in range(len(words)):\n",
    "        #convert all words in lowercase\n",
    "        words[i]=words[i].lower()\n",
    "    return words\n",
    "\n",
    "\n",
    "words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n",
    "#call method Lower()\n",
    "list_Lower=Lower(words)\n",
    "#Print new list\n",
    "print(list_Lower)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 5, 5, 3, 5, 4, 3, 4, 3]\n"
     ]
    }
   ],
   "source": [
    "def Length(words):\n",
    "    for i in range(len(words)):\n",
    "        #convert list having length of each word\n",
    "        words[i]=len(words[i])\n",
    "\n",
    "    return words\n",
    "words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n",
    "#call method\n",
    "list_Length=Length(words)\n",
    "#print new list\n",
    "print(list_Length)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]\n"
     ]
    }
   ],
   "source": [
    "def Low_Up_Len(words):\n",
    "    list=[] #empty list that will store list of upper lower and length of words\n",
    "    temp=[] #list to create list of each word\n",
    "    for i in range(len(words)):\n",
    "        temp.append(words[i].upper())\n",
    "        temp.append(words[i].lower())\n",
    "        temp.append(len(words[i]))\n",
    "        #append temporary list to list\n",
    "        list.append(temp)\n",
    "\n",
    "        #initialize temporary list to empty list\n",
    "        temp=[]\n",
    "\n",
    "\n",
    "    return list\n",
    "\n",
    "\n",
    "words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n",
    "\n",
    "#method call\n",
    "list=Low_Up_Len(words)\n",
    "\n",
    "#print new list\n",
    "print(list)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# e"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['quick', 'brown', 'jumps', 'over', 'lazy']\n"
     ]
    }
   ],
   "source": [
    "def more_4(words):\n",
    "    list=[]\n",
    "    for i in range(len(words)):\n",
    "        #if word length is 4 or more character\n",
    "        if len(words[i])>=4:\n",
    "            \n",
    "            list.append(words[i])\n",
    "\n",
    "\n",
    "    return list\n",
    "\n",
    "\n",
    "words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n",
    "#call method\n",
    "list=more_4(words)\n",
    "#print new list\n",
    "print(list)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
