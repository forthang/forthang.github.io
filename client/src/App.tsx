import React, { useState } from 'react';
import { HomeOutlined } from '@ant-design/icons';
import { Layout, Menu, theme } from 'antd';

const { Header, Content, Footer, Sider } = Layout;


const items = [
  { key: '1', label: 'Show Block A', icon: HomeOutlined },
  { key: '2', label: 'Show Block B', icon: HomeOutlined },
].map((item) => ({
  key: item.key,
  icon: React.createElement(item.icon),
  label: item.label,
}));

const App: React.FC = () => {
  const [mapUrl, setMapUrl] = useState('/map.html'); // State to control map source

  const handleMenuClick = (e: { key: string }) => {
    if (e.key === '1') {
      setMapUrl('/map-block-a.html');
    } else if (e.key === '2') {
      setMapUrl('/map-block-b.html'); 
    }
  };

  return (
    <Layout>
      <Sider
        breakpoint="lg"
        collapsedWidth="0"
        onBreakpoint={(broken) => {
          console.log(broken);
        }}
        width={'15%'}
        onCollapse={(collapsed, type) => {
          console.log(collapsed, type);
        }}
      >
        <div className="demo-logo-vertical" />
        <Menu
          theme="light"
          defaultSelectedKeys={['1']}
          items={items}
          onClick={handleMenuClick} 
        />
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
        <Footer style={{ textAlign: 'center' }}>
          Ant Design ©{new Date().getFullYear()} Created by Ant UED
        </Footer>
      </Layout>
    </Layout>
  );
};

export default App;