import React, { Component } from 'react';


class Fetcher extends Component {
  constructor(props) {
    super(props);

    this.state = {
      data: null,
    };
  }

  componentDidMount() {
    fetch('https://http://34.238.243.88:5000/')
      .then(response => response.json())
      .then(data => this.setState({ data }));
  }

   render() {
    return <Groups people={this.state.data} />;
  }
}
