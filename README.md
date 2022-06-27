# Mini URL Shortener
## Demo
A live version of the application can be found at https://shorten.minidev.io.

![demo](https://user-images.githubusercontent.com/31598368/175831578-9e53ed36-dd8c-4769-b2fb-d9ff94d0534f.gif)

## About
This repo includes a basic URL shortener implementation. It takes a URL and maps it to a short seven character key.

It uses:
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) as a web framework
- [SQLite](https://www.sqlite.org/index.html) as a database
- Vanilla HTML/CSS/JS as a web client

If the intention is to use this at a larger scale, I'd recommend using a full blown RDBMS such as Postgres. SQLite is not designed to scale with high traffic.

## Running the app
To run the application, you'll first need to [install Python on your machine](https://www.python.org/downloads/).

Once you have Python installed, you'll need to open your terminal and install the `Flask` package with `pip`:
```
> pip install Flask
```

From there, we're ready to start the server in development mode. From the root directory of `miniurl`, run the command:
```
> flask run
```

Open your browser and navigate to http://localhost:8080. You should see the app's home page :)

Configuration notes:
- The `BASE_URL` environment variable can be configured by adding a `.env` file to the root of the directory. The default value is `http://localhost:5000/`.

## License
[MIT](LICENSE)
