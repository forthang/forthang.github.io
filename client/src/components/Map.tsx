import { HomeOutlined } from '@ant-design/icons';
import { Layout, Menu } from 'antd';
import React, { useState } from 'react';

const { Header, Content, Sider } = Layout;

const items = [
  { key: '1', label: 'Корпуса МИСИС', icon: <HomeOutlined /> },
  { key: '2', label: 'Общежития МИСИС', icon: <HomeOutlined /> },
];

interface MapProps {
  buildingNames: string[];
  onBuildingSelect: (name: string) => void;
}

export const Map: React.FC<MapProps> = ({ buildingNames, onBuildingSelect }) => {
  const [mapUrl, setMapUrl] = useState('/map.html');

  const handleMenuClick = (e: { key: string }) => {
    if (e.key === '1') {
      setMapUrl('/map-block-a.html');
    } else if (e.key === '2') {
      setMapUrl('/map-block-b.html'); 
    }
  };

  return (
    <Layout>
      <Sider width={'15%'}>
        <div className="demo-logo-vertical" />
        
        <Menu theme="light" defaultSelectedKeys={['1']} items={items} onClick={handleMenuClick} />

        <h3 style={{color:'white'}}>Saved Buildings</h3>
        <Menu mode="inline">
          {buildingNames.map((name, index) => (
            <Menu.Item key={index.toString()} onClick={() => onBuildingSelect(name)}>
              {name}
            </Menu.Item>
          ))}
        </Menu>
      </Sider>
      <Layout>
        <Header />
        <Content style={{ margin: '24px 16px 0' }}>
          <div>
            <iframe
              src={mapUrl}
              title="Map"
              style={{
                width: '85%',
                height: '100vh',
                border: 'none',
                bottom: '0',
                right: '0',
                position: 'absolute',
              }}
            />
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};
