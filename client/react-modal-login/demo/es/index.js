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
<br></br>


<div class = "searchbar">
<div class="row"></div>
  <div class="col-lg-9">
    <div class="input-group">
      <span class="input-group-btn">
        <button class="btn btn-default" type="button">Search</button>
      </span>
      <input type="text" class="form-control" placeholder="Search for..."></input>
    </div>
  </div>
  </div>
  
</div>
    <Sample />

    <script> console.log("datas: \n" + datas);
    console.log("typeof datas: " + typeof(datas));
    console.log("data: " + data);</script>


        <div class="container">
        </div>


    <BubbleChart data = {datas} />
  </div>
  ,

  document.getElementById('app')


);
