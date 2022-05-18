def process_new_bad(repo, cnx, language_codes, new_bad):

    words = new_bad.split()
    if len(words) > 1:
        language_code, bad_word = words[0], ' '.join(words[1:])
        if language_code in language_codes:
            add_bad_word(repo, cnx, language_code, bad_word)
        else:
            print("> ChatBot: Unknown language code '%s' talk to the admin about adding it." % language_code)
    else:
        print("> ChatBot: Usage '%s <LANGUAGE_CODE> <WORD OR PHRASE>'" % NEW_BAD_WORD_STR)


def add_bad_word(repo, cnx, language_code, word):

    query_str = HAS_BAD % (language_code, word)
    cursor = repo.query_server(query_str, cnx)

    row = cursor.next()

    if row[0] == 0:
        query_str = NEW_BAD_WORD_QUERY % (language_code, word)
        repo.query_server(query_str, cnx)
        print("> ChatBot: New bad word '%s' added. You can commit this upon exit." % word)
    else:
        print("> ChatBot: '%s' has already been added." % word)
