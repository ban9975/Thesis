%% Setup the Import Options and import the data
opts = spreadsheetImportOptions("NumVariables", 13);

% Specify sheet and range
opts.Sheet = "stretch";
opts.DataRange = "A1:M82";

% Specify column names and types
opts.VariableNames = ["length", "VarName2", "VarName3", "VarName4", "VarName5", "VarName6", "VarName7", "VarName8", "VarName9", "VarName10", "VarName11", "VarName12", "VarName13"];
opts.VariableTypes = ["double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double"];

% Import the data
resT = readtable("../../3 Data/materials/newCord_20.xlsx", opts, "UseExcel", false);
res = table2array(resT);
% disp(res);
% 2, 4, 6, 8, 10
start_ = [6, 20, 30, 44, 62];
end_ = [10, 28, 42, 60, 82];
% all
% start_ = [2, 6, 12, 20, 30, 44, 62];
% end_ = [4, 10, 18, 28, 42, 60, 82];

xx = [];
yy = [];
zz = [];
for i = 1: 5
    len = res(start_(i), 1);
    for j = start_(i):end_(i)
        for k = 2:11
            xx = [xx; len];
            yy = [yy; res(j, 1)/len];
            zz = [zz; res(j, k)];
        end
    end
end

format long
[sf, gof] = fit([xx, yy], zz, 'poly23')
names = coeffvalues(sf)

p = plot(sf);
alpha(p, 0.3);
hold on;
plot3(xx, yy, zz, '.', 'MarkerSize', 12);
title('Calibration Surface Poly23')
xlabel('Length (cm)')
ylabel('Stretch (%)')
zlabel('Resistance (Ohm)')
hold off;
% legend("old", "new")
set (gca, 'ydir', 'reverse' )

%% Clear temporary variables
clear opts

% 1~3 poly23 ( -0.507608259206674  -0.051576376995301   1.415932591349541   0.000886341814278   0.090505524437016 -1.309889655349229  -0.000880377340776  -0.037931428208841   0.401973570159883) 10^5

% 1~4 poly12 (-0.903937229023085  -0.029036156991141   1.669728932027326   0.039632534017278  -0.762910555201896)10^4
% 1~4 poly22 (-0.895543602695380  -0.026268094474356   1.648768524419510 -0.000520071533507   0.039632534017278  -0.753383097198343)10^4
% 1~4 poly23 ( -0.619036213083872  -0.030800170966657   1.688322998396718  -0.000611641511412   0.057794560352152  -1.531793071531490 0.000488277935669  -0.025444713548645   0.462421072634841)10^5

% all poly12 (-1.822559417203220  -0.016564941358155   3.310589207368547 0.029346431695266  -1.495601716582493) 10^4
% all poly22 (-1.851009466493563  -0.018495900835063   3.370792609269004 0.000157643193582   0.029346431695265  -1.522966899264517) 10^4
% all poly23 (-1.327306628553478  -0.030163327870932   3.618727774341000 0.000186142532652   0.052559495860332  -3.277192984464668 -0.000160177007025  -0.021576583684261   0.986283272944056) 10^5



