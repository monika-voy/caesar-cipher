import unittest
import sys, os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import caesar_cipher


class TestCipher(unittest.TestCase):

    def test_cipher_alpha_only_should_return_ciphered_msg(self):
        expected_result="Ciphered message: oruhp"
        self.assertEqual(expected_result, caesar_cipher.cipher("lorem", 3), msg="Does not return ciphered msg")

    def test_cipher_negative_num_rot_should_return_error_msg(self):
        expected_result="Cannot cipher a message by negative rot value!"
        self.assertEqual(expected_result,caesar_cipher.cipher("lorem",-3), msg="Does not return expected error msg")

    def test_cipher_empty_str_should_return_error_msg(self):
        expected_result="No message to cipher!"
        self.assertEqual(expected_result,caesar_cipher.cipher("",3), msg="Does not return expected error msg")

    def test_cipher_special_char_should_return_ciphered_msg(self):
        expected_result="Ciphered message: $C&'(a)-"
        self.assertEqual(expected_result,caesar_cipher.cipher("!@#$%^&*",3), msg="Does not return ciphered msg")

    def test_cipher_num_should_return_ciphered_msg(self):
        expected_result="Ciphered message: 4567"
        self.assertEqual(expected_result,caesar_cipher.cipher("1234",3), msg="Does not return ciphered msg")

    def test_cipher_ASCII_range_should_rot_from_32(self):
        expected_result="Ciphered message: !"
        self.assertEqual(expected_result, caesar_cipher.cipher("~",2), msg="Does not rot from the beginning of range")

    def test_cipher_polish_alphabet_should_change_to_standard(self):
        expected_result="Ciphered message: oruhp"
        self.assertEqual(expected_result, caesar_cipher.cipher("lóręm",3), msg="Does not change polish letters to standard")

    def test_cipher_input_out_of_defined_ASCII_range_should_return_error_msg(self):
        expected_result="Invalid character in the message!"
        self.assertEqual(expected_result, caesar_cipher.cipher("λφα",3), msg="Does not return Error msg")

    def test_cipher_rot_equals_zero_should_return_error_message(self):
        expected_result="Message not ciphered: lorem"
        self.assertEqual(expected_result, caesar_cipher.cipher("lorem",0), msg="does not return message and ciphered text")

    def test_cipher_rot_other_than_integer_should_return_error_msg(self):
        expected_result="Invalid rot type!"
        self.assertEqual(expected_result,caesar_cipher.cipher("lorem",0.5))
        self.assertEqual(expected_result, caesar_cipher.cipher("lorem","#"))

    def test_cipher_rot_string_type_number_as_word_in_PL_should_return_ciphered_msg(self):
        expected_result="Ciphered message: oruhp"
        self.assertEqual(expected_result,caesar_cipher.cipher("lorem","trzy"))

    def test_cipher_rot_string_type_number_as_word_in_EN_should_return_ciphered_msg(self):
        expected_result="Ciphered message: oruhp"
        self.assertEqual(expected_result,caesar_cipher.cipher("lorem","three"))

    def test_cipher_message_longer_than_200_char_should_return_error_msg(self):
        expected_result="Message must be maximum 200 characters long"
        self.assertEqual(expected_result,caesar_cipher.cipher("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",3))

    def test_cipher_spaces_should_be_left_unciphered(self):
        expected_result="Ciphered message: oruhp lsvxp"
        self.assertEqual(expected_result,caesar_cipher.cipher("lorem ipsum",3))

class TestDecipher(unittest.TestCase):
    def test_decipher_ciphered_message_should_decipher_by_rot(self):
        expected_result="Deciphered message: lorem"
        self.assertEqual(expected_result, caesar_cipher.decipher("oruhp",3))

    def test_decipher_ciphered_message_should_decipher_only_in_defined_ASCII_range(self):
        expected_result="Deciphered message: ~"
        self.assertEqual(expected_result,caesar_cipher.decipher("!",2))

    def test_decipher_ciphered_message_character_out_of_defined_ASCII_scope_should_return_error_message(self):
        expected_result="Invalid character in the ciphered message!"
        self.assertEqual(expected_result,caesar_cipher.decipher("λφα",3))

    def test_decipher_rot_equals_zero_should_return_error_message(self):
        expected_result="Message not deciphered: oruhp"
        self.assertEqual(expected_result,caesar_cipher.decipher("oruhp",0))

    def test_decipher_negative_rot_value_should_return_error_message(self):
        expected_result="Rot value cannot be a negative number"
        self.assertEqual(expected_result,caesar_cipher.decipher("oruhp",-3))

    def test_decipher_empty_str_should_return_error_msg(self):
        expected_result="No ciphered message to decode!"
        self.assertEqual(expected_result,caesar_cipher.decipher("",3), msg="Does not return expected error msg")

    def test_decipher_rot_other_than_integer_should_return_error_msg(self):
        expected_result="Invalid rot type!"
        self.assertEqual(expected_result,caesar_cipher.decipher("lorem",0.5))
        self.assertEqual(expected_result, caesar_cipher.decipher("lorem","#"))

    def test_decipher_rot_string_type_number_as_word_in_PL_should_return_deciphered_msg(self):
        expected_result="Deciphered message: lorem"
        self.assertEqual(expected_result,caesar_cipher.decipher("oruhp","trzy"))

    def test_decipher_rot_string_type_number_as_word_in_EN_should_return_deciphered_msg(self):
        expected_result="Deciphered message: lorem"
        self.assertEqual(expected_result,caesar_cipher.decipher("oruhp","three"))

    def test_decipher_alpha_only_should_return_ciphered_msg(self):
        expected_result="Deciphered message: lorem"
        self.assertEqual(expected_result, caesar_cipher.decipher("oruhp", 3), msg="Does not return ciphered msg")

    def test_decipher_num_should_return_deciphered_msg(self):
        expected_result="Deciphered message: 1234"
        self.assertEqual(expected_result,caesar_cipher.decipher("4567",3), msg="Does not return ciphered msg")

    def test_decipher_special_char_should_return_deciphered_msg(self):
        expected_result="Deciphered message: !@#$%^&*"
        self.assertEqual(expected_result,caesar_cipher.decipher("$C&'(a)-",3), msg="Does not return ciphered msg")

    def test_decipher_message_longer_than_200_char_should_return_error_msg(self):
        expected_result="Ciphered message must be maximum 200 characters long"
        self.assertEqual(expected_result,caesar_cipher.decipher("Oruhp#lsvxp#groru#vlw#dphw,#frqvhfwhwxu#dglslvflqj#holw,#vhg#gr#hlxvprg#whpsru#lqflglgxqw#xw#oderuh#hw#groruh#pdjqd#doltxd.#Xw#hqlp#dg#plqlp#yhqldp#txlv#qrvwuxg#hahuflwdwlrq#xoodpfr#oderulv#qlvl#xw#doltxls#ha#hd#frpprgr#frqvhtxdw.#Gxlv#dxwh#luxuh#groru#lq#uhsuhkhqghulw#lq#yroxswdwh#yholw#hvvh#flooxp#groruh#hx#ixjldw#qxood#sduldwxu.#Hafhswhxu#vlqw#rffdhfdw#fxslgdwdw#qrq#surlghqw,#vxqw#lq#fxosd#txl#riilfld#ghvhuxqw#proolw#dqlp#lg#hvw#oderuxp.",3))

    def test_decipher_spaces_should_be_left_undeciphered(self):
        expected_result="Deciphered message: lorem ipsum"
        self.assertEqual(expected_result,caesar_cipher.decipher("oruhp lsvxp",3))

if __name__ == "__main__":
    unittest.main()