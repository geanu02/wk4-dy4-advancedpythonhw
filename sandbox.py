{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f31a1847",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rotate_paper(number):\n",
    "    _bool = False\n",
    "    _list = [x for x in number]\n",
    "    _dict = { '2' : '2', '5' : '5', '6' : '9', '8' : '8', '9' : '6', '0' : '0' }\n",
    "    idx_left, idx_right = 0, len(_list) - 1\n",
    "    while idx_left <= idx_right:\n",
    "        if _list[idx_left] in _dict:\n",
    "            if _dict[_list[idx_left]] == _list[idx_right]:\n",
    "                _bool = True\n",
    "            else:\n",
    "                return False\n",
    "        else:\n",
    "            return False\n",
    "        idx_left += 1\n",
    "        idx_right -= 1\n",
    "    return _bool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5fee4856",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "rotate_paper(\"906\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "17a20a63",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "def to_camel_case(text):\n",
    "    if text:\n",
    "        _lst = re.findall(r\"[a-zA-Z]+\", text)\n",
    "        _lst2 = []\n",
    "        for i in range(0, len(_lst)):\n",
    "            if i == 0:\n",
    "                lst2.append(_lst[i])\n",
    "        return ''.join(_lst2)\n",
    "    return ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7056e210",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
