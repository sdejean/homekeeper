import fake_filesystem
import homekeeper
import unittest

# pylint: disable=invalid-name
os = None

class HomekeeperTest(unittest.TestCase):
    def setUp(self):
        # pylint: disable=global-statement
        global os
        self.filesystem = fake_filesystem.FakeFilesystem()
        os = fake_filesystem.FakeOsModule(self.filesystem)
        homekeeper.os = os
        homekeeper.util.os = os
        self.homekeeper = homekeeper.Homekeeper({'dotfiles_directory': '.'})

    def tearDown(self):
        del self.filesystem

    #def test_configuration_defaults(self):
    #    self.homekeeper = homekeeper.Homekeeper()
#    self.assertEquals(self.homekeeper.CONFIG_DEFAULTS['dotfiles_directory'],
    #                      self.homekeeper.config['dotfiles_directory'])
    #    self.assertRaises(ValueError, homekeeper.Homekeeper,
    #                      {'dotfiles_directory': os.getenv('HOME')})

    #def test_link_dotfiles(self):
    #    homekeeper.os.getenv = lambda var: '/home/johndoe'
    #    dotfiles_directory = '/home/johndoe/personal/dotfiles'
    #    config = {'dotfiles_directory': dotfiles_directory}
    #    self.filesystem.CreateFile(dotfiles_directory + '/.vimrc')
    #    self.homekeeper = homekeeper.Homekeeper(config)
    #    self.homekeeper.link()
    #    self.assertTrue(os.path.exists('/home/johndoe/personal/dotfiles/'
    #                                   '.vimrc'))
    #    self.assertTrue(os.path.islink('/home/johndoe/.vimrc'))
    #    self.assertTrue(os.path.exists('/home/johndoe/.vimrc'))
    #    self.assertEquals('/home/johndoe/personal/dotfiles/.vimrc',
    #                      os.readlink('/home/johndoe/.vimrc'))
