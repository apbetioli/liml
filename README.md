## Clone the repository
```$ git clone https://github.com/apbetioli/liml.git
$ cd liml```

## Create your heroku app
```$ heroku create```

## Set the environment variables with your mercado livre app client id and client secret
```$ export CLIENT_ID=yourclientid
$ export CLIENT_SECRET=yourclientsecret```

## Test it locally
```$ heroku local web```

## Set the ENV variables in heroku
```$ heroku config:set CLIENT_ID=yourclientid CLIENT_SECRET=yourclientsecret```

## Deploy it to heroku.
```$ git push heroku master```
