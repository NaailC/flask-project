class TestViews(TestBase):
#TEST JENKINS SERVER
    def test_home_get(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)