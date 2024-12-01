import React from 'react';
import { UploadOutlined, UserOutlined, VideoCameraOutlined } from '@ant-design/icons';
import { Layout, Menu } from 'antd';

const { Content, Sider } = Layout;

const items = [UserOutlined, VideoCameraOutlined, UploadOutlined, UserOutlined,UserOutlined,UserOutlined ,UserOutlined,UserOutlined].map(
  (icon, index) => ({
    key: String(index + 1),
    icon: React.createElement(icon),
    label: `building ${index + 1}`,
  }),
);

const App: React.FC = () => {

  return (
    <Layout>
      <Sider 
        breakpoint="lg"
        collapsedWidth="0"
        width="15%"
        theme='light'
        onBreakpoint={(broken) => {
          console.log(broken);
        }}
        onCollapse={(collapsed, type) => {
          console.log(collapsed, type);
        }}

      >
        <div className="demo-logo-vertical" />
        <Menu theme="light" mode="inline" defaultSelectedKeys={['4']} items={items} />
      </Sider>
      <Layout>
        <Content>
          <div
            style={{
              padding: 24,
              minHeight: 360,
              height: "100vh",
            }}
          >
                        <iframe
                src="/map.html"
                title="Map"
                style={{ width: '85%', height: '100vh', border: 'none', bottom:'0', right: '0', position:'absolute'}}
            />
          </div>
        </Content>
        
      </Layout>
    </Layout>
  );
};

export default App;