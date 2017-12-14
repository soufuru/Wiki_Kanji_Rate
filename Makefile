default: jawiki-country.json task.py kanji_rate.txt
	cat jawiki-country.json | python3 task.py | tee -a kanji_rate.txt


add: jawiki-country.json task.py kanji_rate.txt
	echo -e "\n" >> kanji_rate.txt
	cat task.py >> kanji_rate.txt
	cat jawiki-country.json | python3 task.py | tee -a kanji_rate.txt

