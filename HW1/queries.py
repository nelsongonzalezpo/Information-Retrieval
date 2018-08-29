{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "juan {'test2.txt', 'test1.txt'}\n",
      "mar {'test5.txt'}\n",
      "pedro {'test3.txt'}\n",
      "la {'test4.txt'}\n",
      "de {'test4.txt'}\n",
      "paco {'test2.txt'}\n"
     ]
    }
   ],
   "source": [
    "class token:\n",
    "    def __init__(self):\n",
    "        self.files = set()\n",
    "        self.word = \"\"\n",
    "        \n",
    "files = set()\n",
    "words = set()\n",
    "\n",
    "def init():\n",
    "    for i in range (1, 6):\n",
    "        file = \"test%r.txt\" %i\n",
    "        files.add(file)\n",
    "        open(file)\n",
    "        for line in open(file):\n",
    "            tmp = line.split()\n",
    "            for j in tmp:\n",
    "                flag = False\n",
    "                w = token()\n",
    "                w.word = j.lower()\n",
    "                w.files.add(file)\n",
    "                for t in words:\n",
    "                    if t.word == j.lower():\n",
    "                        t.files.add(file)\n",
    "                        flag = True\n",
    "                if flag == False:\n",
    "                    words.add(w)\n",
    "    for t in words:\n",
    "        print(t.word, t.files)\n",
    "        \n",
    "init()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'test2.txt'}\n",
      "{'test4.txt'}\n",
      "{'test5.txt', 'test4.txt', 'test3.txt'}\n",
      "{'test2.txt', 'test1.txt', 'test5.txt', 'test3.txt'}\n"
     ]
    }
   ],
   "source": [
    "def search(term):\n",
    "    for i in words:\n",
    "        if i.word == term:\n",
    "            return i.files\n",
    "        \n",
    "def inverse_search(term):\n",
    "    for i in words:\n",
    "        if i.word == term:\n",
    "            return files ^ i.files\n",
    "\n",
    "def intersection(term1, term2):\n",
    "        return term1.intersection(term2)\n",
    "            \n",
    "print(intersection(search(\"juan\"), search(\"paco\")))\n",
    "print(intersection(search(\"de\"), search(\"la\")))\n",
    "\n",
    "print(inverse_search(\"juan\"))\n",
    "print(intersection(inverse_search(\"de\"), inverse_search(\"la\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "none\n",
      "[{'test2.txt', 'test1.txt', 'test5.txt', 'test3.txt'}]\n",
      "[{'test2.txt', 'test1.txt'}]\n",
      "[{'test2.txt'}]\n",
      "[{'test1.txt'}]\n"
     ]
    }
   ],
   "source": [
    "# use syntax such as \"something & somethingElse & anotherSomethingElse\", \" something & !somethingElse\"\n",
    "def ask(sentence):\n",
    "    tmp = sentence.lower().replace(\" \",\"\").split(\"&\")\n",
    "    queries = []\n",
    "    for i in tmp:\n",
    "        if \"!\" in i:\n",
    "            queries.append(inverse_search(i.replace(\"!\",\"\")))\n",
    "        else:\n",
    "            queries.append(search(i))\n",
    "    query(queries)\n",
    "\n",
    "def query(x):\n",
    "    better_queries = []\n",
    "    if len(x)%2:\n",
    "        j = 0\n",
    "        while j < len(x) - 1:\n",
    "            better_queries.append(intersection (x[j], x[j+1]))\n",
    "            j += 2\n",
    "        better_queries.append(x[j])\n",
    "    else:\n",
    "        j = 0\n",
    "        while j < len(x):\n",
    "            better_queries.append(intersection (x[j], x[j+1]))\n",
    "            j += 2\n",
    "    \n",
    "    if len(better_queries) != 1:\n",
    "        query(better_queries)\n",
    "    else:\n",
    "        if better_queries[0] == set():\n",
    "            print(\"none\")\n",
    "        else:\n",
    "            print (better_queries)\n",
    "                \n",
    "\n",
    "ask(\"juan & pedro\")\n",
    "ask(\"!de & !la\")\n",
    "ask(\"!de & !la & juan\")\n",
    "ask(\"!de & !la & juan & paco\")\n",
    "ask(\"!de & !la & juan & !paco\")"
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
