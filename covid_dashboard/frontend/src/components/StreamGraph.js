import * as React from 'react';
import Paper from '@mui/material/Paper';
import {
  Chart,
  ArgumentAxis,
  AreaSeries,
  Legend,
  Title,
} from '@devexpress/dx-react-chart-material-ui';
import {
  stackOffsetWiggle,
  stackOrderInsideOut,
  curveCatmullRom,
  area,
} from 'd3-shape';

import { Stack, Animation } from '@devexpress/dx-react-chart';

import { booksSale } from './ChartData/data-visualization';

const Area = (props) => {
  const path = area()
    .x(({ arg }) => arg)
    .y1(({ val }) => val)
    .y0(({ startVal }) => startVal)
    .curve(curveCatmullRom);

  return <AreaSeries.Path {...props} path={path} />;
};

const titleStyle = { marginRight: '120px' };
const TitleText = props => <Title.Text {...props} style={titleStyle} />;

export default class Demo extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      data: booksSale,
    };
  }

  render() {
    const { data: chartData } = this.state;

    return (
      <Paper>
        <Chart
          data={chartData}
          style={{ paddingLeft: '20px' }}
        >
          <ArgumentAxis tickFormat={() => tick => tick} />

          <AreaSeries
            name="Mysteries"
            valueField="mysteries"
            argumentField="year"
            seriesComponent={Area}
          />
          <AreaSeries
            name="Science Fiction"
            valueField="scienceFiction"
            argumentField="year"
            seriesComponent={Area}
          />
          <AreaSeries
            name="Romance"
            valueField="romance"
            argumentField="year"
            seriesComponent={Area}
          />
          <AreaSeries
            name="Fantasy"
            valueField="fantasy"
            argumentField="year"
            seriesComponent={Area}
          />
          <AreaSeries
            name="Thrillers"
            valueField="thrillers"
            argumentField="year"
            seriesComponent={Area}
          />
          <Animation />
          <Legend />
          <Title
            text="Book Sales"
            textComponent={TitleText}
          />
          <Stack
            stacks={[
              { series: ['Mysteries', 'Science Fiction', 'Romance', 'Fantasy', 'Thrillers'] },
            ]}
            offset={stackOffsetWiggle}
            order={stackOrderInsideOut}
          />
        </Chart>
      </Paper>
    );
  }
}
