const cheerio = require('cheerio');

(async () => {
    const url = 'https://example.com';
    const responce = await fetch(url);

    const lol = await responce.text();
    const hehe = cheerio.load(lol);

    // console.log(hehe.html());

    // Example of extracting specific elements
    const title = hehe('h1').text();
    const text = hehe('p').text();
    const link = hehe('a').attr('href');

    console.log(title);
    console.log(text);
    console.log(link);
})();