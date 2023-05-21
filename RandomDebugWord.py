import sublime
import sublime_plugin
import random

# This is a simple sublime text plugin that generates a random word to be
# used as a debug print statement in Go, but could and probably will be
# extended to other languages. (Or I find a better way of inserting the word)

# The idea is that you can bind this to a key combination and then insert a quick
# debug print statement prefixed with a random word at a fixed length. This is useful when printf 
# debugging and you want to see the flow of your program. Instead of using random characters
# to build the word, I use a list of Japanese syllables. I didn't want to use words 
# because I don't want to get distracted by the meaning of the word, but I wanted 
# something that was easy to read and pronounce. I chose Japanese because it has a 
# limited set of syllables that work well when combined. I also think it is easier 
# to read than the random characters I was using before. 

syllables_2 = ['ka', 'ki', 'ku', 'ke', 'ko', 'ga', 'gi', 'gu', 'ge', 'go',
                       'sa', 'su', 'se', 'so', 'za', 'ji', 'zu', 'ze', 'zo',
                       'ta', 'te', 'to', 'da', 'de', 'do', 'na', 'ni', 'nu', 
                       'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ba', 'bi', 'bu', 
                       'be', 'bo', 'pa', 'pi', 'pu', 'pe', 'po', 'ma', 'mi', 'mu', 
                       'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 
                       'wa', 'wo']

syllables_3 = ['shi', 'tsu', 'chi', 'nai', 'nei', 'nou', 'sai', 'sei', 'sou',
               'tai', 'tei', 'tou', 'hai', 'hei', 'hou', 'mai', 'mei', 'mou',
               'yai', 'you', 'rai', 'rei', 'rou', 'wai', 'wou',
               'jya', 'jyu', 'jyo', 'gya', 'gyu', 'gyo', 'nya', 'nyu', 'nyo',
               'hya', 'hyu', 'hyo', 'bya', 'byu', 'byo', 'pya', 'pyu', 'pyo',
               'mya', 'myu', 'myo', 'rya', 'ryu', 'ryo']


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
