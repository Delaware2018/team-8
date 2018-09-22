import React from 'react';
import ReactDOM from 'react-dom';

import Sample from './samples/Sample';

require('../less/style.less');

ReactDOM.render(
  <div>
    <h1>Hello World</h1>
    <hr />
    <Sample />
  </div>,
  document.getElementById('app')
);