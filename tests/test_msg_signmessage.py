import unittest
import common
import binascii

from trezorlib.client import CallException

class TestMsgSignmessage(common.TrezorTest):

    def test_sign(self):
        self.setup_mnemonic_nopin_nopassphrase()
        sig = self.client.sign_message('Bitcoin', [0], "This is an example of a signed message.")
        self.assertEqual(sig.address, '14LmW5k4ssUrtbAB4255zdqv3b4w1TuX9e')
        self.assertEqual(binascii.hexlify(sig.signature), '209e23edf0e4e47ff1dec27f32cd78c50e74ef018ee8a6adf35ae17c7a9b0dd96f48b493fd7dbab03efb6f439c6383c9523b3bbc5f1a7d158a6af90ab154e9be80')

    def test_sign_testnet(self):
        self.setup_mnemonic_nopin_nopassphrase()
        sig = self.client.sign_message('Testnet', [0], "This is an example of a signed message.")

        self.assertEqual(sig.address, 'mirio8q3gtv7fhdnmb3TpZ4EuafdzSs7zL')
        self.assertEqual(binascii.hexlify(sig.signature), '209e23edf0e4e47ff1dec27f32cd78c50e74ef018ee8a6adf35ae17c7a9b0dd96f48b493fd7dbab03efb6f439c6383c9523b3bbc5f1a7d158a6af90ab154e9be80')

    def test_too_long(self):
        self.setup_mnemonic_nopin_nopassphrase()

        # Message cannot be longer than 255 bytes
        self.assertRaises(CallException, self.client.sign_message, 'Bitcoin', [0], '1' * 256)

    """
    def test_sign_utf(self):
        self.setup_mnemonic_nopin_nopassphrase()

        words_nfkd = u'Pr\u030ci\u0301s\u030cerne\u030c z\u030clut\u030couc\u030cky\u0301 ku\u030an\u030c u\u0301pe\u030cl d\u030ca\u0301belske\u0301 o\u0301dy za\u0301ker\u030cny\u0301 uc\u030cen\u030c be\u030cz\u030ci\u0301 pode\u0301l zo\u0301ny u\u0301lu\u030a'
        words_nfc = u'P\u0159\xed\u0161ern\u011b \u017elu\u0165ou\u010dk\xfd k\u016f\u0148 \xfap\u011bl \u010f\xe1belsk\xe9 \xf3dy z\xe1ke\u0159n\xfd u\u010de\u0148 b\u011b\u017e\xed pod\xe9l z\xf3ny \xfal\u016f'

        sig_nfkd = self.client.sign_message('Bitcoin', [0], words_nfkd)
        self.assertEqual(sig_nfkd.address, '14LmW5k4ssUrtbAB4255zdqv3b4w1TuX9e')
        self.assertEqual(binascii.hexlify(sig_nfkd.signature), '1fd0ec02ed8da8df23e7fe9e680e7867cc290312fe1c970749d8306ddad1a1eda4e39588e4ec2b6a22dda4ec4f562f06e91129eea9a844a7193812de82d47c496b')

        sig_nfc = self.client.sign_message('Bitcoin', [0], words_nfc)
        self.assertEqual(sig_nfc.address, '14LmW5k4ssUrtbAB4255zdqv3b4w1TuX9e')
        self.assertEqual(binascii.hexlify(sig_nfc.signature), '1fd0ec02ed8da8df23e7fe9e680e7867cc290312fe1c970749d8306ddad1a1eda4e39588e4ec2b6a22dda4ec4f562f06e91129eea9a844a7193812de82d47c496b')
    """

if __name__ == '__main__':
    unittest.main()
