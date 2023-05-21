import sublime
import sublime_plugin
import random

# This is a simple sublime text plugin that generates a random word to be
# used as a debug print statement in Go, but could and probably will be
# extended to other languages. (Or I find a better way of inserting the word)

syllables_2 = ['ka', 'ki', 'ku', 'ke', 'ko', 'na', 'ni', 'nu', 'ne', 'no',
               'sa', 'su', 'se', 'so', 'ta', 'te', 'to', 'ha', 'hi', 
               'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 
               'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo']

syllables_3 = ['shi', 'tsu', 'chi', 'nai', 'nei', 'nou', 'sai', 'sei', 'sou',
               'tai', 'tei', 'tou', 'hai', 'hei', 'hou', 'mai', 'mei', 'mou', 
               'yai', 'you', 'rai', 'rei', 'rou', 'wai', 'wou']


def get_word():
    return random.choice(syllables_3) + random.choice(syllables_2)

class GoDebugPrintCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        word = get_word()
        self.view.run_command("insert_snippet", 
            { 
                "contents": f'fmt.Printf("{word} %v \\n", $0)' 
            }
        )

class GoDebugPrintWordCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        word = get_word()
        self.view.run_command("insert_snippet", 
            { 
                "contents": f'fmt.Printf("{word} \\n")\n$0' 
            }
        )

class DebugWordCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        word = get_word()
        self.view.run_command("insert_snippet", 
            { 
                "contents": f'{word} $0' 
            }
        )
