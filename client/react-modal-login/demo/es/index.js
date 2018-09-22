import React from 'react';
import ReactDOM from 'react-dom';

import SideBar from './side_menu';
import Sample from './samples/Sample';

require('../less/style.less');

ReactDOM.render(
  <div>
    <SideBar pageWrapId={"page-wrap"}/>
    <h1>Hello World</h1>
    <hr />
    <Sample />
  </div>,
  document.getElementById('app')
);