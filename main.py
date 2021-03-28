from instapy import InstaPy
from instapy import smart_run
import random

myusername= ''
mypassword= ''

session = InstaPy(username = myusername,
				  password = mypassword,
				  headless_browser = False)

with smart_run(session):
	session.set_relationship_bounds(enabled=True,
									delimit_by_numbers = True,
									max_followers=500,
									min_followers=30,
									min_following=50)

	# Create a time, x in seconds from 10-25 to avoid any detection
	real_looking_time = random.randint(10,25)
	session.set_action_delays(enabled=True, like=real_looking_time)

	# Follow user?
	session.set_do_follow(True, percentage=10)

	# Configure like tags
	session.set_dont_like(['nsfw'])
	session.like_by_tags(['like4like','follow4follow','followforfollow','likeforlike','followme','like','newcar','newhouse','happy','letsgo'])

	# Comments
	session.set_do_comment(enabled=True, percentage=15)
	session.set_comments(['Awesome', 'Really Cool', 'I like your post','Great','Nice'])

	# Unfollow people who did not engage
	unfollow_amount = random.randint(1,5) # Keep it low, avoids detection
	session.unfollow_users(amount=unfollow_amount, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
