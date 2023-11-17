
# Battleship!

- This Python-based implementation of the classic Battleship game allows a single player to play against the computer, it is played within the Python terminal. 

- The game is played on a square grid where each player has a fleet of ships. The objective is to sink all of your opponent's ships before they sink all of yours.

Visit the deployed website [here](https://battleship-python98-c71c6949cf34.herokuapp.com/).

# 1. How to play

### Game Setup

- Battleship is based on the classic board/paper and pen game, further information on the game can be found on its [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game) "Link to CSS Wikipedia page")

- At the start of the game, players enter their name for a personalized experience.

- The game board is a 6x6 grid.

- Each player, the user and the computer, secretly places 4 ships on their board. Each ship occupies 2 consecutive cells on the grid.

- The ships can be placed either horizontally or vertically, and their placement is random and hidden from the opponent.

- Ships are placed on the board and indicated by an S. Guesses are marked on the board using -, hits are indicated by an X.

### Gameplay

- The user enters their name before the game begins.

- Players take turns to "fire" at the opponent's grid by guessing the coordinates.

- The game asks for row and column numbers separately. Both coordinates start from 1, with 1,1 being the top left corner of the grid. After each guess, the game informs the player whether it was a hit or a miss.

- If a ship is hit at all its coordinates, it is considered sunk.

- The game board does not reveal ship locations, but it does show the results of each player's shots. The player's and computer's scores (number of successful hits) are displayed after each round.

### Winning the Game

- The game continues until all ships of one player are sunk.

- If all of the computer's ships are sunk first, the player wins. Conversely, if all of the player's ships are sunk first, the computer wins.

- The game announces the winner.

# 2. Features

### Existing Feature

- Interactive coordinate input with validation to prevent out-of-bound guesses.



### Home Page

![home-page-image](assets/readme-images/home-page.png)

- Images

  - The images are designed to attract the viewers attention and provide a more interactive experience when viewing the landing/viking timeline.

- Timeline content

  - Contains alternating text and image blocks with information about the timeline of the viking raids in England.

### Article Page

- Ivar the Boneless

![ivar-article-image](assets/readme-images/ivar-article.png)

    - The article page demonstrates a brief but detailed timeline of Ivar the boneless life and qualities, it is designed to keep the information compact and easy to understand to ensure its readers attention is kept.

    - An image of Ivar is displayed next to the article to provide a more dynamic article layout.

### Contact Page

- Contact Form

![feedback-form-image](assets/readme-images/contact-form.png)

    - The form allows the viewers to provide feedback and ask questions directly from the website.

- About Us section

![find-out-more-image](assets/readme-images/find-out-more.png)

    - The about us section allows the user to learn a bit more about the developer/author and directs the viewer to the social media links in the footer.

# 3. Technologies Used

### Languages

- HTML5 and CSS3 were used throughout the project.

- [HTML5](https://fonts.google.com/ "Link to HTML5 Wikipedia page")

- [CSS3](https://en.wikipedia.org/wiki/CSS "Link to CSS Wikipedia page")


### Programs Used

- [Google Fonts](https://en.wikipedia.org/wiki/HTML5 "Link to HTLM5 Wikipedia")
  - Google Fonts was used to import the fonts Lugarismo and Roboto.
  
- [Codeanywhere](https://app.codeanywhere.com/ "Link to Codeanywhere")

  - Codeanywhere was used for writing code, commiting, and then pushing to GitHub..

- [GitHub](https://github.com/ "Link to GitHub")

  - GitHub was used to store the project after pushing.

- [Responsive Design Checker](https://www.responsivedesignchecker.com/)
  - Responsive Design Checker was used in the testing process to check responsiveness on various devices.
- [Am I Responsive?](http://ami.responsivedesign.is/#)

  - Am I Responsive was used to check responsiveness of the site pages across different devices and to gain a view of the whole website on different devices all at once.

- [W3C Markup Validator](https://validator.w3.org/)
  
  - W3C Markup Validator was used to validate the HTML code.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

  - W3C CSS Validator was used to validate the CSS code.

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
  
  - During the development phase, Chrome DevTools were employed for testing, examining, and adjusting HTML elements and CSS styles utilized in the project.

# 4. Testing

### Testing UX

- As a viewer, my goal is to seamlessly explore the website and expand my knowledge on the subject matter at hand.

- The website boasts an intuitive structure that facilitates effortless navigation for viewers, enabling them to easily access the information they seek.

- The navigation bar is consistently visible on all pages, ensuring viewers can locate it effortlessly and navigate the site with ease.

- As a viewer, I also desire a straightforward means of contacting the website's author in case I have any inquiries.

- The footer and dedicated contact page prominently display contact information, making it simple for viewers to reach out with questions or feedback via a convenient feedback form.
Additionally, as a viewer, I hope to discover links to the author's social media profiles.

- The footer conveniently provides links to the author's social media channels.
In my role as a customer, I wish to access further information related to the website's topics. This can be achieved through a link to the Wikipedia page, conveniently located on the contact page.

### Code Validation

- The [W3C Markup Validator](https://validator.w3.org/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) services were used to validate all pages of the project in order to ensure there were no syntax errors.
  
- Index Page

![index-html-validator](assets/readme-images/index-html.png)

- Article Page

![article-html-validator](assets/readme-images/ivar-html.png)

- Contact Page

![contact-html-validator](assets/readme-images/contact-html.png)

- W3C markup validator found no errors on my HTML.

![css-validator](assets/readme-images/css-check.png)

- W3C CSS Validator found no errors or warnings on my CSS.

- I did discover a slight bug that the prettier software caused, certain self closing elements contained a trailing slash that could not be removed, it does not affect the code but an example of the info warning from W3C validator can be seen below.

![prettier-bug](assets/readme-images/prettier-bug.png)

### Testing Tools

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

  - Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.

- Responsiveness

  - [Am I Responsive?](http://ami.responsivedesign.is/#) was used to check responsiveness of the site pages across different devices.

  - [Responsive Design Checker](https://www.responsivedesignchecker.com/) was used to check responsiveness of the site pages on different screen sizes.

  - Chrome DevTools was used to test responsiveness in different screen sizes during the development process.

### Manual Testing

  - The website has been tested on:

    - **Google Chrome**

      No appearance, responsiveness nor functionality issues.

    - **Safari**

      No appearance, responsiveness nor functionality issues.

    - **Mozilla Firefox**

      No responsiveness nor functionality issues.

    - **Microsoft Edge**

      No appearance, responsiveness nor functionality issues.

- Device compatibility

  - The website has been tested on multiple devices, including:

    - **MacBook Air**

      No appearance, responsiveness nor functionality issues.

    - **Lenovo P52 Thinkpad**

      No appearance, responsiveness nor functionality issues.

    - **iPad Pro**

      No appearance, responsiveness nor functionality issues.

    - **iPhone 12**

      No appearance, responsiveness nor functionality issues.

    - **iPhone 8**

      No appearance, responsiveness nor functionality issues.

- Elements Testing

  - All Pages

    - **Navigation Bar**

      - Hovering on the different navigation bar's links will trigger the hover effect, highlighting the link for the customer.

      - Clicking on the navigation bar's links will bring the viewer to the specified page.

    - **Footer**

      - Clicking on the social media links will open the specific website on a new tab.

  - Contact Page

    - Hovering on the submit button within the feedback form section will trigger the hover effect, highlighting the button for the viewer.

  - Feedback Form section

    - When filling out the feedback form, the viewer is required to complete all fields before submitting.

    - Clicking on the link to the Wikipedia page will direct the viewer to the relevant Wikipedia page.

    - The Wikipedia page in the imedia viewfinder is functional and the viewer can scroll through the relevant Wikipedia page directly from the website.

### Accessability

- I used Lighthouse in Chrome Developer Tools to confirm that the dynamics of the color scheme and font choice within the article do not contrast each other negatively.

- Home Page

![ligthouse-home-page](assets/readme-images/lighthouse-home.png)

- Ivar Page

![ligthouse-ivar-page](assets/readme-images/lighthouse-ivar.png)

- Contact Page

![ligthouse-contact-page](assets/readme-images/lighthouse-contact.png)

# 5. Finished Product

![Ivar the Boneless](assets/readme-images/snippit-of-website.png)
   
# 6. Deployment

This website was developed using [Codeanywhere](https://app.codeanywhere.com/), which was then committed and pushed to GitHub using the Codeanywhere terminal.

### GitHub Pages

- Here are the steps to deploy this website to GitHub Pages from its GitHub repository:

  1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).

  2. At the top of the Repository, locate the Settings button on the menu.

  3. Scroll down the Settings page until you locate the Pages section.

  4. Under Source, click the dropdown called None and select Main Branch.

  5. The page will refresh automatically and generate a link to your website.

# 7. Credits

### Content

- All content was written by the developer, however, great inspiration was taken from my fellow Code institue students previous projects.

- Josswe26 VIda Spa project example was a huge inpsiration and greatly assisted in providing the inspiration for the framework stucture of HTML and the structure of the README file, however the content within the inspired framework is my original content.


### Media

- [Pexels](https://www.pexels.com/)

  - Ivar.html image: take by Valiantsin Konan.
  - Longboat image: Valiantsin Konan.

- [Pixabay](https://pixabay.com/)

  - Axes image: taken by ValeriiIavtushenko.
  - Viking drinking image: taken by GioeleFazzeri.
  - Solo viking warrior wielding sword image: taken by GioeleFazzeri.
  - Three knights in wood wielding swords image: taken by GioeleFazzeri.
  - Solar voyer image: taken by Ichigo121212.
  - Knight on horseback: taken by ha11ok.

- [IconFinder](https://www.iconfinder.com/)
  - Facebook logo: Picons.me
  - Instagram logo: Iconfinder
  - Twitter Logo: Iconfinder
  - Mail logo: Feather Icons
  - Favicon logo: https://icons8.com/icons/set/viking

### Code

- [Stack Overflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) were consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

# 8. Acknowledgements

- My friends, for their constructive and honest criticism.

- My mentor Marcel for his helpful guidance, his insight dramatically improved my website quality

- Code Institute for its well developed and diverse lessons that gave me the skills to code this project.