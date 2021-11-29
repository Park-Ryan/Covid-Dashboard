import * as React from 'react';
import Paper from '@mui/material/Paper';
import {
  Chart,
  BarSeries,
  Title,
  ArgumentAxis,
  ValueAxis,
  Legend,
} from '@devexpress/dx-react-chart-material-ui';
import {
  Animation,
  ArgumentScale,
  ValueScale,
} from '@devexpress/dx-react-chart';
import { scaleBand } from 'd3-scale';
import { withStyles } from '@mui/styles';
import { populationPyramid as data } from './ChartData/data-visualization';

const legendStyles = {
  root: {
    display: 'flex',
    margin: 'auto',
    flexDirection: 'row',
  },
};
const legendLabelStyles = theme => ({
  label: {
    paddingTop: theme.spacing(1),
  },
});
const legendItemStyles = {
  item: {
    flexDirection: 'column',
  },
};

const LegendRootBase = ({ classes, ...restProps }) => (
  <Legend.Root {...restProps} className={classes.root} />
);
const LegendLabelBase = ({ classes, ...restProps }) => (
  <Legend.Label {...restProps} className={classes.label} />
);
const LegendItemBase = ({ classes, ...restProps }) => (
  <Legend.Item {...restProps} className={classes.item} />
);
const LegendRoot = withStyles(legendStyles, { name: 'LegendRoot' })(LegendRootBase);
const LegendLabel = withStyles(legendLabelStyles, { name: 'LegendLabel' })(LegendLabelBase);
const LegendItem = withStyles(legendItemStyles, { name: 'LegendItem' })(LegendItemBase);

const Label = ({ text, ...props }) => (
  <ValueAxis.Label {...props} text={`${Math.abs(text)}%`} />
);
const modifyDomain = ([start, end]) => {
  const threshold = Math.ceil(Math.max(Math.abs(start), Math.abs(end)));
  return [-threshold, threshold];
};

export default class Demo extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      data,
    };
  }

  render() {
    const { data: chartData } = this.state;

    return (
      <Paper>
        <Chart
          data={chartData}
          rotated
        >
          <ArgumentScale factory={scaleBand} />
          <ArgumentAxis />
          <ValueScale modifyDomain={modifyDomain} />
          <ValueAxis labelComponent={Label} />

          <BarSeries
            name="Male"
            valueField="male"
            argumentField="age"
            color="#3F7FBF"
          />
          <BarSeries
            name="Female"
            valueField="female"
            argumentField="age"
            color="#F87CCC"
          />
          <Title text="Population Pyramid of the World 2018" />
          <Animation />
          <Legend
            position="bottom"
            rootComponent={LegendRoot}
            itemComponent={LegendItem}
            labelComponent={LegendLabel}
          />
        </Chart>
      </Paper>
    );
  }
}
