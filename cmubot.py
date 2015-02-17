from snapchatbots import SnapchatBot, Snap
from PIL import Image
import zbar

class StorifierBot(SnapchatBot):
    def on_friend_add(self, friend):
        print "Adding %s" % (friend)
        self.add_friend(friend)
    def on_friend_delete(self, friend):
        self.delete_friend(self, friend)
    def on_snap(self, sender, snap):
        data = self.decode_qr(snap.file.name)
        if data != '':
            self.process_data(sender, data)
            return
        if (snap.media_type == 0) and (snap.duration > 5):
            snap.duration = 5
        self.post_story(snap)
    def decode_qr(self, filename):
        scanner = zbar.ImageScanner()
        # configure the reader
        scanner.parse_config('enable')
        # obtain image data
        pil = Image.open(filename).convert('L')
        width, height = pil.size
        raw = pil.tostring()
        # wrap image data
        image = zbar.Image(width, height, 'Y800', raw)
        # scan the image for barcodes
        result = scanner.scan(image)
        # extract results
        if result == 0: 
            return ''
        else:
            for symbol in image:
                pass
            # clean up
            del(image)
            #Assuming data is encoded in utf8
            return symbol.data.decode(u'utf-8')
    def process_data(self, sender, data):
        if data == 'stef':
            snap = Snap.from_file('poopoo.png')
            self.send_snap([sender], snap)
        return

if __name__ == '__main__':
    with open('credentials.txt') as f:
        user = f.readline().strip()
        pw = f.readline().strip()
    bot = StorifierBot(user, pw)
    # Get all the new friends
    friends = bot.get_friends()
    for user in bot.get_added_me():
        if user not in friends:
            print "Adding %s" % (user)
            bot.add_friend(user)
    bot.listen()
