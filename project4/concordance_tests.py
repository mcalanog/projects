import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

   def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file1.txt")
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

   def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

   def test_03(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

   def test_error(self):
       conc = Concordance()
       with self.assertRaises( FileNotFoundError ):
           conc.load_stop_table( "eroor.txt" )
       with self.assertRaises( FileNotFoundError ):
           conc.load_concordance_table( "error.txt" )

   def test_empty_file(self):
       conc = Concordance()
       conc.load_stop_table( "stop_words.txt" )
       conc.load_concordance_table( "empty_file.txt" )
       conc.write_concordance( "empty_con.txt" )
       self.assertTrue( filecmp.cmp( "empty_con.txt", "empty_file.txt" ) )

   def test_single_word(self):
       con = Concordance()
       con.load_stop_table( "stop_words.txt" )
       con.load_concordance_table( "one_word.txt" )
       con.write_concordance( "one_con.txt" )
       self.assertTrue( filecmp.cmp( "one_con.txt", "one_sol.txt" ) )
   def test_WP(self):
       con = Concordance()
       con.load_stop_table( "stop_words.txt" )
       con.load_concordance_table( "War_And_Peace.txt" )
       con.write_concordance( "WP_con.txt" )

   def test_similar(self):
       con = Concordance()
       con.load_stop_table( "stop_words.txt" )
       con.load_concordance_table( "dictionary_a-c.txt" )
       con.write_concordance( "blah.txt" )

if __name__ == '__main__':
   unittest.main()
