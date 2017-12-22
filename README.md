# Spanish Conjugation Flashcards
This is a python script that creates text files, containing conjugations for the spanish verbs you provided, ready to be imported into Quizlet.

# Example
__Supported types as indicated in the script itself__
`supported_types = ['presentIndicative', 'preteritIndicative','imperfectIndicative', 'presentSubjunctive']`
__Contents of words.txt__
```
ganar
llevar
```
__Running the script__
`python conjugation-flashcards.py words.txt`
__After the script runs__
Several files are created, such as `presentIndicative.txt`,
`preteritIndicative.txt`, `imperfectIndicative.txt`, `presentSubjunctive.txt`.
__Output of presentIndicative.txt__
```
yo ganar	 gano
tú ganar	 ganas
él/ella/Ud. ganar	 gana
nosotros ganar	 ganamos
vosotros ganar	 ganáis
ellos/ellas/Uds. ganar	 ganan
yo enseñar	 enseño
tú enseñar	 enseñas
él/ella/Ud. enseñar	 enseña
nosotros enseñar	 enseñamos
vosotros enseñar	 enseñáis
ellos/ellas/Uds. enseñar	 enseñan
```
### Usage
- The words that the user wants to conjugate must be in a text file, delimited by `\n`.
- The script outputs separate text files, one for each type of mood&tense.
- All possible moods & tenses are specified in the script.
- Each text file contains rows of the following format `<pronoun> <verb in infinitive mood><tab><conjugated verb>`
- If the script is run several times, conjugations will be appended to the end, even if they are already in the file. 

### Installation
All the necessary packages are specified in `environment.yml`.
__For conda users__
`conda env create`

### Development
I make changes to the jupyter notebook file, and when I am ready to commit, I run the following command to export a `.py` file.
`jupyter nbconvert --to script conjugation-flashcards.ipynb`

### Todos
This was a quick script I put together, to aid me in memorizing different conjugations of spanish verbs. There are several improvements I can think of. 
- Write tests
- Allow user to specify supported types without having to modify the python script itself
- Allow user to exclude certain pronouns (temporary fix: use grep to remove lines containing the unneeded pronoun from the text files)

