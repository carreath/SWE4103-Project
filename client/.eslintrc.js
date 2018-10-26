module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/essential',
    '@vue/airbnb',
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-param-reassign': 'off',
    'no-shadow': 'off',
    'arrow-body-style': 'off',
    'linebreak-style': 'off',
    'no-unused-expressions': 'off',
    'arrow-parens': 'off',
    'prefer-const': 'off',
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
};
