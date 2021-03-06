ARG = task.py

#上書き
default: jawiki-country.json ${ARG} kanji_rate.txt
	cat jawiki-country.json | python3 ${ARG} | tee -a kanji_rate.txt

#出力のみ
only: jawiki-country.json ${ARG}
	cat jawiki-country.json | python3 ${ARG}


#コードを変更した場合に使う奴
add: jawiki-country.json ${ARG} kanji_rate.txt
	echo -e "\n" >> kanji_rate.txt
	cat ${ARG} >> kanji_rate.txt
	cat jawiki-country.json | python3 ${ARG} | tee -a kanji_rate.txt

