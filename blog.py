from robotpageobjects import Page, robot_alias
from robot.utils import asserts
#from rails_database import get_post_id
from database.rails_database import get_post_id

class BlogHomePage(Page):
    """ Models mu Ruby on Rails Blog at:
        http://localhost:3000/posts"""

    name = "Blog"

    uri = "/posts"
    
    selectors = {
        "new": "link=New Post",
        "show": "link=Show",
        "nth edit link": "xpath=(//a[@href='/posts/{n}/edit'])",
        #"destroy": "link=Destroy",
        #"nth destroy link": "xpath=(//a[@href='/posts/{n}'])"#//a[@data-method='delete'])",
        "nth destroy link": "xpath=(//a[@href='/posts/{n}' and text()='Destroy'])",
    }
    
    def click_in_new_post(self):
        locator = self.resolve_selector("new")
        self.click_link(locator)
        return BlogPostPage()
    
    def click_in_destroy(self, title, body):
        post_id = get_post_id(title, body)
        locator = self.resolve_selector("nth destroy link", n=post_id)
        #locator = self.resolve_selector("destroy")
        self.click_link(locator)
        alert = self._current_browser().switch_to_alert().accept()
        return BlogHomePage()

    def click_in_edit(self, title, body):
        post_id = get_post_id(title, body)
        locator = self.resolve_selector("nth edit link", n=post_id)
        self.click_link(locator)
        return BlogEditPostPage()
 
    def click_in_show(self):
        locator = self.resolve_selector("show")
        self.click_link(locator)
        return BlogPostPage()
 
    @robot_alias("__name__body_should_contain")
    def body_should_contain(self, str, ignore_case=True):
        ref_str = str.lower() if ignore_case else str
        ref_str = ref_str.encode("utf-8")
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_true(ref_str in body_txt, "body text does not contain %s" %ref_str)
        return self

    @robot_alias("__name__body_should_not_contain")
    def body_should_not_contain(self, str, ignore_case=True):
        ref_str = str.lower() if ignore_case else str
        ref_str = ref_str.encode("utf-8")
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_true(ref_str not in body_txt, "body text does contain %s" %ref_str)
        return self


class BlogPostPage(Page):
    """Models my Ruby on Rails Blog For example:
    http://localhosts:3000/posts/new """
   
    
    uri = "/posts/new"

    selectors = {
        "title": "id=post_title",
        "body": "id=post_body",
        "create post": "name=commit",
        "back": "link=Back",
        "comment": "id=comment_body",
        "create comment": "name=commit",
    }

    def click_in_back(self):
        locator = self.resolve_selector("back")
        self.click_link(locator)
        return BlogHomePage()

    def type_in_title_box(self, txt):
        self.input_text("title", txt)
        return self
        
    def type_in_body_box(self, txt):
        self.input_text("body", txt)
        return self

    def type_in_comment_box(self, txt):
        self.input_text("comment", txt)
        return self
    
    def click_in_create_post(self):
        self.click_button("create post")
        return BlogHomePage()
    
    def click_in_add_comment(self):
        self.click_button("create comment")
        return BlogHomePage()
    
    @robot_alias("__name__body_should_contain")
    def body_should_contain(self, str, ignore_case=True):
        ref_str = str.lower() if ignore_case else str
        ref_str = ref_str.encode("utf-8")
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_true(ref_str in body_txt, "body text does not contain %s" %ref_str)
        return self

class BlogEditPostPage(Page):


    uri = "/posts/{blog_id}/edit"

    selectors = {
        "title": "id=post_title",
        "body": "id=post_body",
        "update post": "name=commit",
    }

    def edit_title_box(self, txt):
        self.input_text("title", txt)
        return self

    def edit_body_box(self, txt):
        self.input_text("body", txt)
        return self 
    
    def click_in_update_post(self):
        self.click_button("update post")
        return self
   
    @robot_alias("__name__body_should_contain")
    def body_should_contain(self, str, ignore_case=True):
        ref_str = str.lower() if ignore_case else str
        ref_str = ref_str.encode("utf-8")
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_true(ref_str in body_txt, "body text does not contain %s" %ref_str)
        return self

