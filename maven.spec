# To Build:
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# wget http://apache.claz.org/maven/maven-3/3.3.3/binaries/apache-maven-3.3.3-bin.tar.gz  -O ~/rpmbuild/SOURCES/apache-maven-3.3.3-bin.tar.gz
# wget https://raw.github.com/chukka/rpm-maven/master/maven.spec -O ~/rpmbuild/SPECS/maven.spec
# rpmbuild -bb ~/rpmbuild/SPECS/maven.spec

Name:           maven
Version:        3.3.3
Release:        1
Summary:        Apache Maven software project management and comprehension tool.
License:        Apache Software License
URL:            http://ant.apache.org/
Group:          Development/Build Tools
Source0:        apache-maven-%{version}-bin.tar.gz
Requires:       jdk
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

%prep
%setup -q -n apache-maven-%{version}

%build

install -d -m 755 %{buildroot}/apps/%{name}
cp -R %{_builddir}/apache-maven-%{version}/* %{buildroot}/apps/%{name}/

# Make it the default
install -d -m 755 %{buildroot}/etc/profile.d/
echo 'export MAVEN_HOME=/apps/%{name}' > %{buildroot}/etc/profile.d/%{name}.sh
echo 'export PATH=/apps/%{name}/bin:$PATH' >> %{buildroot}/etc/profile.d/%{name}.sh

%clean
rm -rf %{buildroot}

%post
echo
echo "You will need to exit your shell to have mvn in your default path."
echo "Or run the following"
echo '  export MAVEN_HOME=/apps/maven'
echo '  export PATH=/apps/maven/bin:$PATH'
echo

%files
/apps/%{name}/
/etc/profile.d/%{name}.sh

