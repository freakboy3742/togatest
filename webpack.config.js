var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
      './assets/js/togatest.js'
  ],

  output: {
      path: path.resolve('./assets/bundles/'),
      //   filename: "[name]-[hash].js",
        filename: "[name].js",
      // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
      publicPath: 'http://localhost:3000/assets/bundles/',
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './webpack.stats.json'})
  ],

  // module: {
  //   loaders: [
  //     {
  //         test: /\.jsx?$/,
  //         exclude: /node_modules/,
  //         loaders: ['babel'],
  //     },
  //   ],
  // },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js']
  }
}
