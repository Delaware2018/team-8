import React from 'react';
import ReactDOM from 'react-dom';

import SideBar from './side_menu';
import Sample from './samples/Sample';

import BubbleChart from './bubblecharts';
import datas from './data.json';

require('../less/style.less');

ReactDOM.render(

  <div>





    <SideBar pageWrapId={"page-wrap"}/>

<div class="col-xs-9"></div>
<div class = "col-xs-3">
<button type="button" class="btn btn-info">Business Info</button>
<button type="button" class="btn btn-success">Sign In</button>
<button type="button" class="btn btn-primary">Register</button>
</div>


    <Sample />

    <script> console.log("datas: \n" + datas);
    console.log("typeof datas: " + typeof(datas));
    console.log("data: " + data);</script>

    <BubbleChart data = {datas} />
  </div>
  ,
  document.getElementById('app')
);
